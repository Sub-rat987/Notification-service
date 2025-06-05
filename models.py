from sqlalchemy import create_engine, Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from config import DATABASE_URI

Base = declarative_base()
engine = create_engine(DATABASE_URI)
SessionLocal = sessionmaker(bind=engine)

class Notification(Base):
    __tablename__ = 'notifications'

    id = Column(Integer, primary_key=True)
    user_id = Column(String, nullable=False)
    message = Column(String, nullable=False)
    type = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "message": self.message,
            "type": self.type,
            "timestamp": self.timestamp.isoformat()
        }

Base.metadata.create_all(engine)

def save_notification(notification_obj):
    session = SessionLocal()
    try:
        session.add(notification_obj)
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()

def get_notifications(user_id):
    session = SessionLocal()
    try:
        notifications = session.query(Notification).filter_by(user_id=user_id).all()
        return [n.to_dict() for n in notifications]
    finally:
        session.close()