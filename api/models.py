from django.db import models


TASK_TYPE_CHOICES = {"HM": "Home", "WK": "Work", "OT": "Other"}


class Task(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(blank=True)
    task_type = models.ChoiceField(choices=TASK_TYPE_CHOICES)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_complete = models.BooleanField()
