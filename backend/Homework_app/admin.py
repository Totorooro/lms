from django.contrib import admin
from .models import Homework

@admin.register(Homework)
class HomeworkAdmin(admin.ModelAdmin):
    list_display = ('title', 'subject', 'group', 'due_date', 'status', 'assigned_by')
    list_filter = ('status', 'subject', 'group')
    search_fields = ('title', 'description')
    ordering = ('-due_date',)