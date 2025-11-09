from django.db import models
from schedule_app.models import Group

class Event(models.Model):
    STATUS_CHOICES = [
        ('upcoming', 'Предстоящее'),
        ('ongoing', 'Сейчас'),
        ('completed', 'Прошедшее'),
    ]
    
    TYPE_CHOICES = [
        ('sport', 'Спорт'),
        ('competition', 'Соревнование'),
        ('conference', 'Конференция'),
        ('courses', 'Курсы'),
        ('seminar', 'Семинар'),
        ('cultural', 'Культурное'),
    ]

    title = models.CharField(max_length=255, verbose_name='Заголовок')
    description = models.TextField(max_length=255, blank=True, verbose_name='Описание')
    start_date = models.DateField(verbose_name="Дата начала")
    start_time = models.TimeField(blank=True, null=True, verbose_name="Время начала")
    end_date = models.DateField(blank=True, null=True, verbose_name="Дата окончания")
    end_time = models.TimeField(blank=True, null=True, verbose_name="Время окончания")
    location = models.CharField(max_length=255, blank=True, verbose_name="Место")
    organizer = models.CharField(max_length=255, blank=True, verbose_name="Организатор")
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='upcoming', verbose_name="Статус")
    type_status = models.CharField(max_length=100, choices=TYPE_CHOICES, default='cultural', verbose_name='Тип мероприятия')
    participants_limit = models.PositiveIntegerField(default=0, verbose_name="Лимит участников") 
    current_participants = models.PositiveIntegerField(default=0, verbose_name="Текущие участники")
    groups = models.ManyToManyField(Group, blank=True, verbose_name="Группы")

    class Meta:
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия"

    def __str__(self):
        return self.title
    
    @property
    def progress(self):
        if self.participants_limit > 0:
            return f"{self.current_participants} / {self.participants_limit}"
        return None