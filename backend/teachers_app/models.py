from django.db import models

class Teacher(models.Model):
    full_name = models.CharField(max_length=255, verbose_name="ФИО")
    position = models.CharField(max_length=255, verbose_name="Должность", blank=True)
    department = models.CharField(max_length=255, verbose_name="Кафедра", blank=True)
    email = models.EmailField(blank=True, verbose_name="Email")
    phone = models.CharField(max_length=20, blank=True, verbose_name="Телефон")
    office = models.CharField(max_length=50, blank=True, verbose_name="Кабинет")
    consultation_hours = models.TextField(blank=True, verbose_name="Часы консультаций")

    class Meta:
        verbose_name = "Преподаватель"
        verbose_name_plural = "Преподаватели"
        ordering = ['full_name']

    def str(self):
        return self.full_name