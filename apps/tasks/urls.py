from django.urls import path

from apps.tasks.views import (
    TaskListCreateAPIView,
    TaskStatusChangeAPIView,
    TaskStatusDoneListAPIView,
    TaskStatusUndoneListAPIView,
    TaskUpdateDestroyAPIView,
)

urlpatterns = [
    path(
        "<slug:list_slug>/<slug:task_slug>/status/",
        TaskStatusChangeAPIView.as_view(),
        name="task-status-change",
    ),
    path(
        "<slug:list_slug>/done/", TaskStatusDoneListAPIView.as_view(), name="task-done"
    ),
    path(
        "<slug:list_slug>/undone/",
        TaskStatusUndoneListAPIView.as_view(),
        name="task-undone",
    ),
    path("<slug:list_slug>/", TaskListCreateAPIView.as_view(), name="task-list-create"),
    path(
        "<slug:list_slug>/<slug:task_slug>/",
        TaskUpdateDestroyAPIView.as_view(),
        name="task-update-destroy",
    ),
]
