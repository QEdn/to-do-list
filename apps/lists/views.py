import logging

from django.contrib.auth import get_user_model
from rest_framework import generics, permissions

from apps.lists.models import List
from apps.lists.permissions import IsOwner
from apps.lists.serializers import ListSerializer

logger = logging.getLogger(__name__)
User = get_user_model()


class ListListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(author=user)
        logger.info(f"List {serializer.data.get('title')} created by {user.first_name}")

    def get_queryset(self):
        return List.objects.filter(author=self.request.user).order_by("-created_at")


class ListUpdateDestroyAPIView(generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = List.objects.all()
    lookup_field = "slug"
    serializer_class = ListSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]
