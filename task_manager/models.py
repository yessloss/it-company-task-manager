from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class TaskType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Worker(AbstractUser):
    position = models.ForeignKey(Position, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "worker"
        verbose_name_plural = "workers"

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"

    def get_absolute_url(self):
        return reverse("task_manager:worker_detail", kwargs={"pk": str(self.pk)})


PRIORITY = (
        ("1", "Urgent and important"),
        ("2", "Urgent and not important"),
        ("3", "Not urgent and important"),
        ("4", "Not urgent and not important"),
    )


class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateField()
    is_completed = models.BooleanField()
    priority = models.CharField(max_length=255, choices=PRIORITY, default="4")
    task_type = models.ForeignKey(TaskType, on_delete=models.CASCADE)
    assignees = models.ManyToManyField(Worker, related_name="staff")

    def __str__(self):
        return (f"{self.name} "
                f"{self.description} "
                f"{self.deadline} "
                f"{self.is_completed} "
                f"{self.priority}")

    def get_absolute_url(self):
        return reverse("task_manager:task_detail", kwargs={"pk": self.pk})
