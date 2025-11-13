from django.contrib import admin
from .models import Teacher

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'position', 'department', 'email', 'phone', 'office')
    list_filter = ('department', 'position')
    search_fields = ('full_name', 'email', 'phone')
    ordering = ('full_name',)
    fieldsets = (
        (None, {
            'fields': ('full_name', 'position', 'department')
        }),
        ('Контакты', {
            'fields': ('email', 'phone', 'office', 'consultation_hours'),
            'classes': ('collapse',)
        }),
    )