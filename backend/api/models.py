from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = [
        ('student', 'Студент'),
        ('teacher', 'Преподаватель'),
        ('admin', 'Администратор')
    ]
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='student',
        verbose_name="Роль"
    )
    group = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name="Группа"
    )
    direction = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Направление"
    )
    
    