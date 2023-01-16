from django.urls import path
from .views import (index,
                    TaskTypeListView,
                    TaskTypeCreateView,
                    TaskTypeUpdateView,
                    TaskTypeDeleteView,
                    PositionListView,
                    PositionUpdateView,
                    PositionDeleteView,
                    PositionCreateView, WorkerListView, WorkerDetailView, WorkerCreateView, WorkerUpdateView,
                    WorkerDeleteView)

urlpatterns = [
    path("", index, name="index"),
    path("task_type/", TaskTypeListView.as_view(), name="task_type_list"),
    path("task_type/create/", TaskTypeCreateView.as_view(), name="task_type_create_"),
    path("task_type/<int:pk>/update/", TaskTypeUpdateView.as_view(), name="task_type_update"),
    path("task_type/<int:pk>/delete/", TaskTypeDeleteView.as_view(), name="task_type_delete"),
    path("position/", PositionListView.as_view(), name="position_list"),
    path("position/create/", PositionCreateView.as_view(), name="position_create_"),
    path("position/<int:pk>/update/", PositionUpdateView.as_view(), name="position_update"),
    path("position/<int:pk>/delete/", PositionDeleteView.as_view(), name="task_type_delete"),
    path("worker/", WorkerListView.as_view(), name="worker_list"),
    path("worker/<int:pk>/", WorkerDetailView.as_view(), name="worker_detail"),
    path("worker/create/", WorkerCreateView.as_view(), name="worker_create"),
    path("worker/<int:pk>/update/", WorkerUpdateView.as_view(), name="worker_update"),
    path("worker/<int:pk>/delete/", WorkerDeleteView.as_view(), name="worker_delete"),
]

app_name = "task_manager"
