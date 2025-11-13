from django.contrib import admin
from .models import Exam

@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ('subject', 'group', 'exam_type', 'date', 'time', 'location', 'teacher')
    list_filter = ('exam_type', 'group', 'date')
    search_fields = ('subject__name', 'teacher', 'location')
    ordering = ('date', 'time')
    fieldsets = (
        (None, {
            'fields': ('subject', 'group', 'teacher', 'exam_type')
        }),
        ('Дата и время', {
            'fields': ('date', 'time', 'location')
        }),
        ('Дополнительно', {
            'fields': ('description',),
            'classes': ('collapse',)
        }),
    )
