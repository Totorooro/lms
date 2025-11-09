from rest_framework import serializers
from .models import Department, Teacher, Subject, TeacherSubject

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'

class TeacherSubjectSerializer(serializers.ModelSerializer):
    subject_name = serializers.CharField(source='subject.name', read_only=True)
    
    class Meta:
        model = TeacherSubject
        fields = ['id', 'subject', 'subject_name', 'course']

class TeacherSerializer(serializers.ModelSerializer):
    department_name = serializers.CharField(source='department.name', read_only=True)
    subjects = TeacherSubjectSerializer(many=True, read_only=True, source='teachersubject_set')
    
    class Meta:
        model = Teacher
        fields = [
            'id', 'first_name', 'last_name', 'middle_name', 
            'position', 'department', 'department_name',
            'email', 'phone', 'office', 'consultation_schedule',
            'subjects'
        ]