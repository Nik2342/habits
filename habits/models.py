from django.db import models
from django.db.models import SET_NULL

from users.models import User


class Habit(models.Model):
    user = models.ForeignKey(
        User, verbose_name="Пользователь", on_delete=SET_NULL, null=True, blank=True
    )
    place = models.CharField(
        max_length=150,
        blank=True,
        null=True,
        verbose_name="Место",
        help_text="Место, в котором необходимо выполнять привычку",
    )
    time = models.TimeField(
        verbose_name="Время",
        null=True,
        blank=True,
        help_text="Укажите время выполнения привычки",
    )
    action = models.CharField(
        verbose_name="Действие",
        max_length=150,
        blank=True,
        null=True,
        help_text="Укажите действие",
    )
    is_pleasant_habit = models.BooleanField(verbose_name="Признак приятной привычки")
    related_habit = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Связанная привычка",
    )
    periodicity = models.FloatField(
        default=1,
        verbose_name="Периодичность",
        help_text="Количество дней выполнения в неделю",
    )
    award = models.CharField(null=True, blank=True, verbose_name="Вознаграждение")
    complete_time = models.FloatField(
        verbose_name="Время на выполнение в секундах", null=True, blank=True
    )
    is_public = models.BooleanField(verbose_name="Признак публичности", default=False)

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"

    def __str__(self):
        return f"{self.user} будет {self.action} в {self.time} в {self.place}"
