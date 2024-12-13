from plyer import notification

# Send Notification
notification.notify(
    title="Reminder",
    message="Take a break and stretch!",
    app_name="Python Notifier",
    timeout=10
)