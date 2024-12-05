from django.urls import path

from .views import ListListCreateAPIView, ListUpdateDestroyAPIView

urlpatterns = [
    path("", ListListCreateAPIView.as_view(), name="list-list-create"),
    path(
        "<slug:slug>/",
        ListUpdateDestroyAPIView.as_view(),
        name="list-update-destroy",
    ),
]
