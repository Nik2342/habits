from rest_framework.generics import (
    ListAPIView,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from habits.models import Habit
from habits.paginators import HabitPagination
from habits.serializers import HabitSerializer, PublicHabitSerializer
from users.permissions import IsOwner


class HabitViewSet(ModelViewSet):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    pagination_class = HabitPagination

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        course = serializer.save()
        course.owner = self.request.user
        course.save()

    def get_permissions(self):
        if self.action == "create":
            self.permission_classes = (IsAuthenticated,)
        else:
            self.permission_classes = (IsOwner,)
        return super().get_permissions()


class PublicHabitListAPIView(ListAPIView):
    serializer_class = PublicHabitSerializer

    def get_queryset(self):
        return Habit.objects.filter(is_public=True)
