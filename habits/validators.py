from rest_framework.serializers import ValidationError


def validate_fields(habit):
    if habit.award and habit.related_habit:
        raise ValidationError(
            "Нельзя одновременно указывать связанную привычку и вознаграждение"
        )
    if habit.is_pleasant_habit:
        if habit.award:
            raise ValidationError("Приятная привычка не может иметь вознаграждение.")
        if habit.related_habit:
            raise ValidationError(
                "Приятная привычка не может иметь связанную привычку."
            )
    if habit.related_habit and not habit.related_habit.is_pleasant_habit:
        raise ValidationError("Связанная привычка должна быть приятной.")


def validate_periodicity(periodicity):
    if periodicity <= 0:
        raise ValidationError("Необходимо выполнять привычку хотя бы раз в неделю.")
    elif periodicity > 7:
        raise ValidationError("Периодичность не должна превышать 7 дней.")


def validate_time(time):
    if time * 60 > 86400:
        raise ValidationError("Время выполнения привычки не может быть больше дня")
    elif time == 0:
        raise ValidationError("Время выполнения не может быть равным 0")
