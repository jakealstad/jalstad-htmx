from typing import List

from ninja import NinjaAPI

from .models import Task
from .schemas import TaskSchemaOut

api = NinjaAPI()


@api.get("hello/")
def hello(request):
    return "Hello world"


@api.get("get_tasks/", response=List[TaskSchemaOut])
def get_tasks(request):
    tasks = Task.objects.all()
    return list(tasks)
