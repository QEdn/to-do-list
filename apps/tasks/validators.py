from django.shortcuts import get_object_or_404
from rest_framework.exceptions import NotFound, PermissionDenied

from apps.lists.models import List
from apps.tasks.models import Task


def is_owner(self, list_slug):
    if self.request.user != get_object_or_404(List, slug=list_slug).author:
        raise PermissionDenied("You do not have permission to perform this action.")
    return True


def task_exists(list_slug, task_slug):
    task = Task.objects.filter(list__slug=list_slug, slug=task_slug).first()
    if not task:
        raise NotFound("Task not found")
    return task


def check_task(self):
    list_slug = self.kwargs.get("list_slug")
    task_slug = self.kwargs.get("task_slug")
    if not is_owner(self, list_slug):
        raise PermissionDenied("You do not have permission to perform this action.")
    return task_exists(list_slug, task_slug)
