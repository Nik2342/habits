from rest_framework import serializers
from habits.models import Habit
from habits.validators import validate_fields, validate_periodicity, validate_time


class HabitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Habit
        fields = "__all__"

    def validate(self, data):
        habit_instance = self.instance or Habit()

        for attr, value in data.items():
            setattr(habit_instance, attr, value)

        validate_fields(habit_instance)

        periodicity = data.get(
            "periodicity", getattr(self.instance, "periodicity", None)
        )
        if periodicity is not None:
            validate_periodicity(periodicity)

        time = data.get("time", getattr(self.instance, "time", None))
        if time is not None:
            validate_time(time)

        return data


class PublicHabitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Habit
        fields = (
            "name",
            "is_pleasant_habit",
        )
