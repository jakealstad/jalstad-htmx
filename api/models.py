from django.contrib.auth.models import User
from django.db import models

TASK_TYPE_CHOICES = [("home", "Home"), ("work", "Work"), ("other", "Other")]


class Task(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(blank=True)
    task_type = models.CharField(choices=TASK_TYPE_CHOICES, max_length=12)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_complete = models.BooleanField()

    def __str__(self):
        return f"{self.name} - {self.task_type} - {self.description} - is_complete: {self.is_complete}"
