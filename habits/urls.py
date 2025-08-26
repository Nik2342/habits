from django.urls import path
from rest_framework import routers

from habits.apps import HabitsConfig
from habits.views import HabitViewSet, PublicHabitListAPIView

app_name = HabitsConfig.name

router = routers.DefaultRouter()
router.register(r"habit", HabitViewSet)

urlpatterns = [
    path("public_habits/", PublicHabitListAPIView.as_view(), name="public_habit_list"),
] + router.urls
