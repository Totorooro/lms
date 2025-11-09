from django.db import models

class Department(models.Model):
    """Модель кафедры"""
    name = models.CharField(max_length=200, verbose_name="Название кафедры")
    short_name = models.CharField(max_length=50, verbose_name="Сокращенное название", blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Кафедра"
        verbose_name_plural = "Кафедры"

class Teacher(models.Model):
    """Модель преподавателя"""
    # Основная информация
    first_name = models.CharField(max_length=100, verbose_name="Имя")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    middle_name = models.CharField(max_length=100, verbose_name="Отчество", blank=True)
    
    # Должность
    POSITION_CHOICES = [
        ('professor', 'Профессор'),
        ('associate_professor', 'Доцент'),
        ('assistant', 'Ассистент'),
        ('senior_lecturer', 'Старший преподаватель'),
        ('lecturer', 'Преподаватель'),
    ]
    position = models.CharField(max_length=50, choices=POSITION_CHOICES, verbose_name="Должность")
    
    # Кафедра
    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name="Кафедра")
    
    # Контактная информация
    email = models.EmailField(verbose_name="Email", blank=True)
    phone = models.CharField(max_length=20, verbose_name="Телефон", blank=True)
    office = models.CharField(max_length=20, verbose_name="Кабинет", blank=True)
    
    # График консультаций
    consultation_schedule = models.TextField(
        verbose_name="График консультаций", 
        blank=True,
        help_text="Например: Пн 16:00-18:00, Чт 14:00-16:00"
    )
    
    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}"
    
    def get_full_name(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}"
    
    class Meta:
        verbose_name = "Преподаватель"
        verbose_name_plural = "Преподаватели"

class Subject(models.Model):
    """Модель предмета (наша собственная, не связанная с schedule_app)"""
    name = models.CharField(max_length=200, verbose_name="Название предмета")
    short_name = models.CharField(max_length=50, verbose_name="Сокращенное название", blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Предмет"
        verbose_name_plural = "Предметы"

class TeacherSubject(models.Model):
    """Связь преподавателей с предметами которые они ведут"""
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name="Преподаватель")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name="Предмет")
    course = models.CharField(max_length=50, verbose_name="Курс", blank=True, help_text="Например: ИУ7-71Б")
    
    class Meta:
        verbose_name = "Преподаватель-Предмет"
        verbose_name_plural = "Преподаватели-Предметы"
    
    def __str__(self):
        return f"{self.teacher} - {self.subject} ({self.course})"