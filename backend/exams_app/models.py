from django.db import models
from schedule_app.models import Subject, Group

class Exam(models.Model):
    EXAM_TYPE_CHOICES = [
        ('credit', 'Зачет'),
        ('diff_credit', 'Диф. зачет'),
        ('exam', 'Экзамен'),
    ]

    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name="Предмет")
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name="Группа")
    teacher = models.CharField(max_length=255, verbose_name="Преподаватель")
    exam_type = models.CharField(max_length=20, choices=EXAM_TYPE_CHOICES, verbose_name="Тип")
    date = models.DateField(verbose_name="Дата")
    time = models.TimeField(verbose_name="Время")
    location = models.CharField(max_length=100, verbose_name="Аудитория")
    description = models.TextField(blank=True, verbose_name="Описание")

    class Meta:
        verbose_name = "Экзамен"
        verbose_name_plural = "Экзамены"
        ordering = ['date', 'time']

    def str(self):
        return f"{self.get_exam_type_display()} — {self.subject} ({self.date})"