from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class UserCreationFormCustom(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'role', 'group')

class UserChangeFormCustom(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'role', 'group')

class UserAdmin(BaseUserAdmin):
    add_form = UserCreationFormCustom
    form = UserChangeFormCustom
    model = User
    list_display = ['username', 'email', 'role', 'group', 'is_staff', 'is_active', 'password']
    list_filter = ['role', 'group', 'is_staff', 'is_active']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('email', 'role', 'group')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'role', 'group', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('username', 'email')
    ordering = ('username',)

admin.site.register(User, UserAdmin)