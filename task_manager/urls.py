from django.urls import path
from .views import index, TaskTypeListView, TaskTypeCreateView, TaskTypeUpdateView, TaskTypeDeleteView

urlpatterns = [
    path("", index, name="index"),
    path("task_type/", TaskTypeListView.as_view(), name="task_type_list"),
    path("task_type/create/", TaskTypeCreateView.as_view(), name="task_type_create_"),
    path("task_type/<int:pk>/update/", TaskTypeUpdateView.as_view(), name="task_type_update"),
    path("task_type/<int:pk>/delete/", TaskTypeDeleteView.as_view(), name="task_type_delete"),
]

app_name = "task_manager"
