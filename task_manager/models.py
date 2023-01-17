from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class TaskType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return {self.name}


class Position(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return {self.name}


class Worker(AbstractUser):
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"

    def get_absolute_url(self):
        return reverse("task_manager:worker_detail", kwargs={"pk": self.pk})


class Task(models.Model):
    PRIORITY = ["Urgent and important",
                "Urgent and not important",
                "Not urgent and important",
                "Not urgent and not important"]
    name = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateTimeField()
    is_completed = models.BooleanField()
    priority = models.CharField(max_length=255, choices=PRIORITY)
    task_type = models.ForeignKey(TaskType, on_delete=models.CASCADE)
    assignees = models.ManyToManyField(Worker)

    def __str__(self):
        return (f"{self.name} "
                f"{self.description} "
                f"{self.deadline} "
                f"{self.is_completed} "
                f"{self.priority}")
