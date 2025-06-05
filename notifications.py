import random

def send_email(message):
    if random.random() < 0.2:
        raise Exception("Email service failed")
    print(f"Sending EMAIL: {message}")

def send_sms(message):
    if random.random() < 0.2:
        raise Exception("SMS service failed")
    print(f"Sending SMS: {message}")

def send_in_app(message):
    print(f"Sending IN-APP Notification: {message}")

def dispatch_notification(notif_type, message):
    if notif_type == "email":
        send_email(message)
    elif notif_type == "sms":
        send_sms(message)
    elif notif_type == "in-app":
        send_in_app(message)
    else:
        raise ValueError("Unsupported notification type")
