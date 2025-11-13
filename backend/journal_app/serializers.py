from rest_framework import serializers
from .models import Grade
from schedule_app.models import Subject

class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = '__all__'

class JournalSummarySerializer(serializers.Serializer):
    overall_performance = serializers.FloatField()
    total_grades = serializers.IntegerField()
    subjects_count = serializers.IntegerField()
    subjects = serializers.ListField(child=serializers.DictField())