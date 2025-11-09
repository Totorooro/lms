from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'start_date', 'location', 'organizer', 'status', 'type_status', 'progress']
    list_filter = ['status', 'type_status']
    search_fields = ['title']
    ordering = ['id']
    filter_horizontal = ['groups']
