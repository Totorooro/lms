from django.db import models
from django.utils import timezone
from schedule_app.models import Subject, Group
from api.models import User

class Homework(models.Model):
    STATUS_CHOICES = [
        ('pending', 'В ожидании'),
        ('urgent', 'Срочно'),
        ('overdue', 'Просрочено'),
    ]

    title = models.CharField(max_length=255, verbose_name='Заголовок')
    description = models.TextField(blank=True, verbose_name='Описание')
    due_date = models.DateField(verbose_name="Дата сдачи")
    due_time = models.TimeField(blank=True, null=True, verbose_name="Время сдачи")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name="Предмет")
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name="Группа")  
    assigned_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_homeworks', verbose_name="Преподаватель")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name="Статус")

    class Meta:
        verbose_name = "Домашнее задание"
        verbose_name_plural = "Домашние задания"
        ordering = ['-due_date']

    def str(self):
        return f"{self.title} ({self.subject})"

    def update_status(self):
        now = timezone.now().date()
        if self.due_date < now:
            self.status = 'overdue'
        elif self.due_date == now or (self.due_date - now).days <= 1:  
            self.status = 'urgent'
        else:
            self.status = 'pending'
        self.save(update_fields=['status'])