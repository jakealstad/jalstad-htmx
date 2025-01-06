import random

from api.models import TASK_TYPE_CHOICES, Task
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from lorem_text import lorem

TASK_TYPE_CHOICES = [choice[0] for choice in TASK_TYPE_CHOICES]


class Command(BaseCommand):
    help = "Generate n random tasks with lorem ipsum text"

    def add_arguments(self, parser):
        parser.add_argument("n", type=int, help="Number of random tasks to create")

    def handle(self, *args, **kwargs):
        n = kwargs["n"]

        if not n:
            self.stdout.write(self.style.SUCCESS("No tasks created."))
            return

        # Ensure there are some users to assign tasks
        users = User.objects.all()
        if not users.exists():
            self.stdout.write(
                self.style.ERROR(
                    "No users available to assign tasks. Please create some users first."
                )
            )
            return

        for i in range(n):
            user = random.choice(users)
            task_type = random.choice(TASK_TYPE_CHOICES)
            name = lorem.words(3).capitalize()  # Generate a short name
            description = lorem.paragraph()  # Generate random paragraph for description
            is_complete = random.choice([True, False])

            Task.objects.create(
                name=name,
                description=description,
                task_type=task_type,
                owner=user,
                is_complete=is_complete,
            )

            self.stdout.write(self.style.SUCCESS(f"Task {i + 1}/{n} created: {name}"))

        self.stdout.write(self.style.SUCCESS(f"Successfully created {n} random tasks."))
