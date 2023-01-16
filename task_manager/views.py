from django.shortcuts import render

from task_manager.models import TaskType, Task, Position, Worker

def index(request):
    num_task_types = TaskType.objects.count()
    num_tasks = Task.objects.count()
    num_positions = Position.objects.count()
    num_workers = Worker.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_task_types": num_task_types,
        "num_tasks": num_tasks,
        "num_positions": num_positions,
        "num_workers" : num_workers,
        "num_visits": num_visits + 1,
    }

    return render(request, "task_manager/index.html", context=context)


