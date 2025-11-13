from rest_framework import serializers
from .models import Exam

class ExamSerializer(serializers.ModelSerializer):
    days_until = serializers.SerializerMethodField()
    subject_name = serializers.CharField(source='subject.name', read_only=True)
    group_name = serializers.CharField(source='group.name', read_only=True)

    class Meta:
        model = Exam
        fields = [
            'id', 'subject', 'subject_name', 'group', 'group_name', 'teacher',
            'exam_type', 'date', 'time', 'location', 'description', 'days_until'
        ]

    def get_days_until(self, obj):
        from datetime import date
        today = date.today()
        delta = (obj.date - today).days
        return delta if delta >= 0 else 0