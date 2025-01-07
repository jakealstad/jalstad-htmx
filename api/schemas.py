from typing import Literal

from ninja.orm import create_schema

from .models import Task

TaskSchema = create_schema(Task)


class TaskSchemaOut(TaskSchema):
    task_type: Literal["home", "work", "other"]
