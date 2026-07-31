from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Task(models.Model):

    CATEGORY_CHOICES = [
        ("daily", "Daily"),
        ("work", "Work"),
        ("study", "Study"),
        ("health", "Health"),
        ("finance", "Finance"),
        ("shopping", "Shopping"),
        ("personal", "Personal"),
        ("other", "Other"),
    ]

    PRIORITY_CHOICES = [
        ("high", "High"),
        ("medium", "Medium"),
        ("low", "Low"),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="tasks"
    )

    title = models.CharField(max_length=200)

    description = models.TextField(blank=True)

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default="daily"
    )

    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default="medium"
    )

    due_date = models.DateField()

    reminder_datetime = models.DateTimeField(null=True,blank=True)

    reminder_sent = models.BooleanField(default=False)

    status = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title