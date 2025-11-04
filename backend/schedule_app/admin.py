from django.contrib import admin
from .models import Subject, Group, Lesson

@admin.register(Subject)
class Subjects(admin.ModelAdmin):
    list_display = ["id", "name", "description"]
    ordering = ["id"]
    list_per_page = 30
    search_fields = ["name"]
    list_editable = ["name"]


@admin.register(Group)
class Groups(admin.ModelAdmin):
    list_display = ["id", "name", "direction", "description"]
    ordering = ["id"]
    search_fields = ["name"]

@admin.register(Lesson)
class Lessons(admin.ModelAdmin):
    list_display = ["id", "subject", "type", "start_time", "end_time",  "day", "classroom", "teacher", "group", "week_type"]
    ordering = ["id"]
    list_per_page = 30
    search_fields = ["subject"]
    list_editable = ["type", "week_type"]
    list_filter = ["subject", "group"]