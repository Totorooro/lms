from django.db import models
from teachers_app.models import Teacher, TeacherSubject  # Импортируем из teachers_app


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
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name="Группа")
    week_type = models.CharField(max_length=20, choices=WEEK_TYPE_CHOICES, default='every', verbose_name="Тип недели")

    # СТАРОЕ поле — для миграции (можно удалить позже)
    teacher_old = models.CharField(max_length=100, blank=True, null=True, verbose_name="Преподаватель (старое)")

    # НОВОЕ поле — правильная связь с teachers_app.Teacher

    teacher = models.ForeignKey(
        'teachers_app.Teacher',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='lessons',
        verbose_name="Преподаватель"
    )

    teachersubject = models.ForeignKey(
        'teachers_app.TeacherSubject',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='schedule_lessons',
        verbose_name="Преподаватель + Предмет + Курс"
    )

    # Опционально: связь с конкретной парой "Преподаватель + Предмет + Курс"
    teachersubject = models.ForeignKey(
        TeacherSubject,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='lessons',
        verbose_name="Преподаватель + Предмет + Курс"
    )

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
        ordering = ['day', 'start_time']

    def __str__(self):
        teacher_name = self.teacher.get_full_name() if self.teacher else "—"
        return f"{self.subject} — {teacher_name} ({self.get_type_display()})"
    
    
