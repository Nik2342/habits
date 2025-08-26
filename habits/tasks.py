from datetime import timezone, timedelta

import requests
from celery import shared_task
from django.conf import settings
from habits.models import Habit


@shared_task
def send_message():
    now = timezone.now()
    time_start = now + timedelta(minutes=1)
    time_end = now + timedelta(minutes=5)

    habits = Habit.objects.select_related("user").filter(
        time__gte=time_start,
        time__lte=time_end,
        notified=False,
        user__tg_chat_id__isnull=False,
    )

    for habit in habits:
        if not habit.user.tg_name:
            continue
        message = f"Напоминание! Выполните полезную привычку {habit.action} в месте {habit.place}."
        params = {
            "text": message,
            "chat_id": habit.user.tg_name,
        }
        requests.get(
            f"{settings.TELEGRAM_URL}{settings.TELEGRAM_TOKEN}/sendMessage",
            params=params,
        )
