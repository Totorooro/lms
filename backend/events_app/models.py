from django.db import models
<<<<<<< HEAD
from schedule_app.models import Group
=======
from django.utils import timezone
from datetime import datetime, time
from schedule_app.models import Group
from api.models import User 
>>>>>>> 9df53b4cc22ac6cf660fc88c39f35d33284bf285

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
<<<<<<< HEAD
=======
    participants = models.ManyToManyField(User, blank=True, related_name='registered_events', verbose_name="Участники") 
>>>>>>> 9df53b4cc22ac6cf660fc88c39f35d33284bf285

    class Meta:
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия"

    def __str__(self):
        return self.title
    
    @property
    def progress(self):
        if self.participants_limit > 0:
            return f"{self.current_participants} / {self.participants_limit}"
<<<<<<< HEAD
        return None
=======
        return None

    def update_status(self):
        now = timezone.now()
        start_datetime = datetime.combine(self.start_date, self.start_time or time(0, 0))
        start_datetime = timezone.make_aware(start_datetime) if not timezone.is_aware(start_datetime) else start_datetime
        
        end_datetime = datetime.combine(self.end_date or self.start_date, self.end_time or time(23, 59))
        end_datetime = timezone.make_aware(end_datetime) if not timezone.is_aware(end_datetime) else end_datetime
        
        if now < start_datetime:
            self.status = 'upcoming'
        elif start_datetime <= now <= end_datetime:
            self.status = 'ongoing'
        else:
            self.status = 'completed'
        self.save(update_fields=['status'])

    
>>>>>>> 9df53b4cc22ac6cf660fc88c39f35d33284bf285
