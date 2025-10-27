from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название предмета")
    description = models.TextField(blank=True, verbose_name="Описание")

    class Meta:
        verbose_name = "Предмет"
        verbose_name_plural = "Предметы"

    
    def __str__(self):
        return self.name
    

class Group(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Название группы")
    direction = models.CharField(max_length=255, blank=True, null=True, verbose_name="Направление")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"

    def __str__(self):
        return self.name



class Lesson(models.Model):
    TYPE_CHOICES = [
        ('lecture', 'Лекция'),
        ('lab', 'Лаб. работа'),
        ('seminar', 'Семинар'),
        ('practice', 'Практика'),
    ]
    DAY_CHOICES = [
        (1, 'Понедельник'),
        (2, 'Вторник'),
        (3, 'Среда'),
        (4, 'Четверг'),
        (5, 'Пятница'),
        (6, 'Суббота'),
        (7, 'Воскресенье'),
    ]

    WEEK_TYPE_CHOICES = [
        ('every', 'Каждая неделя'),
        ('odd', 'Нечетная неделя'),
        ('even', 'Четная неделя'),
    ]

    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name="Предмет")
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, verbose_name="Тип занятия")
    start_time = models.TimeField(verbose_name="Время начала")
    end_time = models.TimeField(verbose_name="Время окончания")
    day = models.IntegerField(choices=DAY_CHOICES, verbose_name="День недели")
    classroom = models.CharField(max_length=50, verbose_name="Аудитория")
    teacher = models.CharField(max_length=100, blank=True, null=True, verbose_name="Преподаватель")
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name="Группа")
    week_type = models.CharField(max_length=20, choices=WEEK_TYPE_CHOICES, default='every', verbose_name="Тип недели")


    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"

    def __str__(self):
        return f"{self.subject}"
    