from django.db import models
from django.contrib.auth.models import AbstractUser
from schedule_app.models import Group

class User(AbstractUser):
    ROLE_CHOICES = [
        ('student', 'Студент'),
        ('teacher', 'Преподаватель'),
        ('admin', 'Администратор')
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='student', verbose_name="Роль")
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True, related_name='students', verbose_name="Группа")
    

    
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username
