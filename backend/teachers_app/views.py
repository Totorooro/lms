from rest_framework import viewsets, filters
from rest_framework.permissions import AllowAny  
from .models import Department, Teacher, Subject, TeacherSubject
from .serializers import DepartmentSerializer, TeacherSerializer, SubjectSerializer, TeacherSubjectSerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [AllowAny]  
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'short_name']

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all().prefetch_related('teachersubject_set__subject')
    serializer_class = TeacherSerializer
    permission_classes = [AllowAny]  
    filter_backends = [filters.SearchFilter]
    search_fields = ['first_name', 'last_name', 'middle_name', 'department__name']

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [AllowAny]  
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'short_name']

class TeacherSubjectViewSet(viewsets.ModelViewSet):
    queryset = TeacherSubject.objects.all().select_related('teacher', 'subject')
    serializer_class = TeacherSubjectSerializer
    permission_classes = [AllowAny]  