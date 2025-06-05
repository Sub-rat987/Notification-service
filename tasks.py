from celery import Celery
from config import CELERY_BROKER_URL, CELERY_RESULT_BACKEND
from notifications import dispatch_notification
from models import Notification, save_notification
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

celery = Celery('tasks', broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)

@celery.task(bind=True, max_retries=3, default_retry_delay=5)
def send_notification_task(self, user_id, message, notif_type):
    logger.info(f"Processing notification task: user_id={user_id}, type={notif_type}")
    
    try:
        # Step 1: Send the notification
        logger.info("Dispatching notification...")
        dispatch_notification(notif_type, message)
        logger.info("Notification dispatched successfully")
        
        # Step 2: Save to database
        logger.info("Creating notification object...")
        notif = Notification(user_id=user_id, message=message, type=notif_type)
        logger.info("Saving notification to database...")
        save_notification(notif)
        logger.info("Task completed successfully")
        
    except Exception as exc:
        logger.error(f"Task failed with exception: {str(exc)}")
        logger.info(f"Retrying... (attempt {self.request.retries + 1}/{self.max_retries})")
        raise self.retry(exc=exc)