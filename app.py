from flask import Flask, request, jsonify
from tasks import send_notification_task
from models import get_notifications

app = Flask(__name__)

@app.route("/notifications", methods=["POST"])
def send_notification():
    data = request.json
    user_id = data.get("user_id")
    message = data.get("message")
    notif_type = data.get("type")

    if not user_id or not message or notif_type not in ["email", "sms", "in-app"]:
        return jsonify({"error": "Invalid input"}), 400

    send_notification_task.delay(user_id, message, notif_type)
    return jsonify({"status": "queued"}), 202

@app.route("/users/<user_id>/notifications", methods=["GET"])
def get_user_notifications(user_id):
    notifications = get_notifications(user_id)
    return jsonify(notifications), 200

if __name__ == "__main__":
    app.run(debug=True)
