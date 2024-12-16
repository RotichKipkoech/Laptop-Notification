# pip install plyer
from plyer import notification

# Send and Show Notification
notification.notify(
    title="Reminder",
    message="Hey!!! Take a break and stretch!",
    app_name="Python Notifier",
    timeout=10
)