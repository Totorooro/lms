from django.utils import timezone
from django.db import models
from schedule_app.models import Subject
from api.models import User  

class Grade(models.Model):
    value = models.FloatField(verbose_name="Оценка")  
    date = models.DateField(default=timezone.now, verbose_name="Дата")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name="Предмет")
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='grades', verbose_name="Студент")
    comment = models.TextField(blank=True, verbose_name="Комментарий")

    class Meta:
        verbose_name = "Оценка"
        verbose_name_plural = "Оценки"
        ordering = ['-date']

    def str(self):
        return f"{self.value} for {self.subject} ({self.student})"