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
    list_display = [
        "id", "subject", "type", "start_time", "end_time",
        "day", "classroom", "teacher_display", "group", "week_type"
    ]
    ordering = ["id"]
    list_per_page = 30
    search_fields = ["subject__name"]
    list_editable = ["type", "week_type"]
    list_filter = ["subject", "group"]

    # ДОБАВЬ ЭТОТ МЕТОД:
    def teacher_display(self, obj):
        return obj.teacher.get_full_name() if obj.teacher else "—"
    teacher_display.short_description = "Преподаватель"
    teacher_display.admin_order_field = 'teacher__last_name'