# Notification Service

This is a lightweight Flask-based notification microservice designed to send and manage notifications for users. The service exposes a REST API endpoint to handle notification requests and delegates the processing to background tasks. It is modular, easy to extend, and suitable for integration with larger microservices-based systems.

## Project Structure

notification_service/
├── app.py             # Main Flask app and route handler
├── tasks.py           # Function to execute notification sending logic
├── models.py          # Function to retrieve user-specific notifications
├── notifications.py   # Utility module to send notifications (currently mocked)
├── config.py          # Configuration (currently not used)
├── requirements.txt   # Python dependencies
└── .venv/             # Python virtual environment (excluded from version control)

## How it works

- The service exposes a single POST endpoint at `/notifications`.
- The client sends a JSON payload containing:
  - `user_id`: ID of the user to send the notification to
  - `message`: Text content of the notification
  - `type`: Type/category of the notification
- The Flask route receives the request and calls `send_notification_task()`, passing the relevant parameters.
- Notifications are sent using the `send_notification()` function from `notifications.py`.
- Notifications for a given user can also be retrieved using `get_notifications(user_id)` from `models.py`.

## Example request

POST /notifications
Content-Type: application/json

```json
{
  "user_id": "123",
  "message": "Hello from the notification service",
  "type": "info"
}
```

## Setup Instructions

1. Clone the repository:

```bash
git clone git@github.com:Sub-rat987/Notification-service.git
cd Notification-service
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/Scripts/activate  # On Windows
# or
source .venv/bin/activate      # On Linux/macOS
```

3. Install the dependencies:

```bash
pip install -r requirements.txt
```

4. Run the Flask app:

```bash
python app.py
```

The service will be available at http://localhost:5000/notifications

## Notes

- The project currently uses mock logic for sending notifications and retrieving stored messages.
- It is structured in a way that allows easy integration of a message broker (e.g., RabbitMQ, Celery) or database in the future.
- Logging, persistence, and message queue integration can be added as next steps.

