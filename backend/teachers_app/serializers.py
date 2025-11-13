from rest_framework import serializers
from .models import Teacher

class TeacherSerializer(serializers.ModelSerializer):
    subjects = serializers.SerializerMethodField()

    class Meta:
        model = Teacher
        fields = ['id', 'full_name', 'position', 'department', 'email', 'phone', 'office', 'consultation_hours', 'subjects']

    def get_subjects(self, obj):
        # Получаем предметы из Lesson, где teacher.full_name совпадает с lesson.teacher
        from schedule_app.models import Lesson
        subjects = Lesson.objects.filter(teacher=obj.full_name).values('subject__name').distinct()
        return [s['subject__name'] for s in subjects]