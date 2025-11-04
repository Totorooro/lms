from rest_framework import serializers
from .models import Subject, Lesson, Group

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ["id", "name", "description"]
        

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name', 'direction', 'description']


class LessonSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer(read_only=True)
    group = GroupSerializer(read_only=True)

    class Meta:
        model = Lesson
        fields = ['id', 'subject', 'type', 'start_time', 'end_time', 'day', 'classroom', 'teacher', 'group', 'week_type']