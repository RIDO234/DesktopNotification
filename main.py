from plyer import notification

notification_title = "Selam Windows"
notification_message = "Masaüstü Bildirim Test"

notification.notify(
    title = notification_title,
    message = notification_message,
    app_icon = None,
    timeout = 10,
    toast = False
)