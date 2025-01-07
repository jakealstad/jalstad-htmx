from typing import List

from ninja import NinjaAPI

from .models import Task
from .schemas import TaskSchemaOut

api = NinjaAPI()


@api.get("hello/")
def hello(request):
    return "Hello world"


@api.get("get_tasks/", response=List[TaskSchemaOut])
def get_tasks(request, limit: int = 10, offset: int = 0, task_type: str = None):
    tasks = (
        Task.objects.filter(task_type=task_type) if task_type else Task.objects.all()
    )
    return list(tasks[offset : offset + limit])
