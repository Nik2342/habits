from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):

    def setUp(self) -> None:
        super().setUp()
        self.user = User.objects.create(email="test@test.test")
        self.habit = Habit.objects.create(
            place="Работа", action="Улыбаться", is_pleasant_habit=False, user=self.user
        )
        self.client.force_authenticate(user=self.user)

    def test_habit_retrieve(self):
        url = reverse("habits:habit-detail", args=(self.habit.pk,))
        response = self.client.get(url)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("action"), self.habit.action)

    def test_habit_create(self):
        url = reverse("habits:habit-list")
        data = {
            "place": "Улица",
            "action": "Ходить 10000 шагов",
            "is_pleasant_habit": False,
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.all().count(), 2)

    def test_habit_update(self):
        url = reverse("habits:habit-detail", args=(self.habit.pk,))
        data = {"place": "Спортзал"}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("place"), "Спортзал")

    def test_habit_delete(self):
        url = reverse("habits:habit-detail", args=(self.habit.pk,))

        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.all().count(), 0)

    def test_habit_list(self):
        url = reverse("habits:habit-list")

        response = self.client.get(url)
        data = response.json()

        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.habit.pk,
                    "place": self.habit.place,
                    "time": None,
                    "action": self.habit.action,
                    "is_pleasant_habit": False,
                    "periodicity": 1,
                    "award": None,
                    "is_public": False,
                    "user": 3,
                    "complete_time": None,
                    "related_habit": None,
                }
            ],
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)
