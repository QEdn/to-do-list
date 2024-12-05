from django.urls import path

from apps.profiles.views import ProfileDetailAPIView, avatar_upload_api_view

urlpatterns = [
    path("me/", ProfileDetailAPIView.as_view(), name="profile-me"),
    path("avatar/", avatar_upload_api_view, name="avatar-upload"),
]
