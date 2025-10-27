from django.contrib import admin
from .models import Subject, Group, Lesson

@admin.register(Subject)
class Subjects(admin.ModelAdmin):
    list_display = ["id", "name", "description"]


@admin.register(Group)
class Groups(admin.ModelAdmin):
    list_display = ["id", "name", "direction", "description"]

@admin.register(Lesson)
class Lessons(admin.ModelAdmin):
    list_display = ["id", "subject", "type", "start_time", "end_time",  "day", "classroom", "teacher", "group", "week_type"]