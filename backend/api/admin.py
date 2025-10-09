from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "first_name", "last_name", "username", "email", "role", "group", "direction", "is_active", "is_staff", "is_superuser"]
    fields = ["first_name", "last_name", "username", "email", "role", "group", "direction"]
    ordering = ["id"]
    list_per_page = 10
    search_fields = ["last_name"]
    list_display_links = ["id"]