from django.contrib import admin

from habits.models import Habit


@admin.register(Habit)
class CourseAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "action",
        "place",
        "is_pleasant_habit",
    )
    search_fields = (
        "name",
        "place",
    )
