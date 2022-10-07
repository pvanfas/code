# users/functions.py


def create_notification(request, notification_type, instance=False):
    who = request.user
    subject = NotificationSubject.objects.get(code=notification_type)
    superusers = User.objects.filter(is_superuser=True)

    if notification_type == "customer_created":

        for superuser in superusers:
            # create notification for super user
            if not superuser == who:
                Notification.objects.create(
                    user=superuser, subject=subject, who=who, customer=instance
                )

            # Add other users here
