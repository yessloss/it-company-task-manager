from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from task_manager.models import Task
from django import forms


class TaskForm(forms.ModelForm):
    assignees = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Task
        fields = "__all__"