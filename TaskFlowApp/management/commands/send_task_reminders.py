from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.utils import timezone
from django.conf import settings

from TaskFlowApp.models import Task


class Command(BaseCommand):

    help = "Send reminder emails for tasks"

    def handle(self, *args, **kwargs):

        now = timezone.now()

        tasks = Task.objects.filter(
            reminder_datetime__lte=now,
            reminder_sent=False
        ).exclude(
            user__email=""
        )

        self.stdout.write(
            f"Current time: {now}"
        )

        self.stdout.write(
            f"Tasks found: {tasks.count()}"
        )

        for task in tasks:

            send_mail(
                subject=f"TaskFlow Reminder: {task.title}",

                message=(
                    f"Hello {task.user.username},\n\n"
                    f"This is a reminder for your task:\n\n"
                    f"Task: {task.title}\n"
                    f"Description: {task.description}\n"
                    f"Due Date: {task.due_date}\n\n"
                    f"Please complete your task on time.\n\n"
                    f"Regards,\n"
                    f"TaskFlow"
                ),

                from_email=settings.EMAIL_HOST_USER,

                recipient_list=[
                    task.user.email
                ],

                fail_silently=False
            )

            task.reminder_sent = True
            task.save(update_fields=["reminder_sent"])

            self.stdout.write(
                self.style.SUCCESS(
                    f"Reminder sent for: {task.title}"
                )
            )