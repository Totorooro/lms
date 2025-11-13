from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db.models import Avg, Count
from .serializers import GradeSerializer, JournalSummarySerializer
from .models import Grade
from schedule_app.models import Subject

class GradeViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = GradeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Grade.objects.filter(student=self.request.user).order_by('-date')

class JournalSummaryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        grades = Grade.objects.filter(student=user)
        
        if not grades.exists():
            return Response({'overall_performance': 0, 'total_grades': 0, 'subjects_count': 0, 'subjects': []})

        overall_performance = grades.aggregate(Avg('value'))['value__avg'] or 0
        total_grades = grades.count()
        subjects_count = grades.values('subject').distinct().count()
        
        subjects_data = []
        for subject in Subject.objects.filter(id__in=grades.values_list('subject', flat=True).distinct()):
            subject_grades = grades.filter(subject=subject)
            avg_grade = subject_grades.aggregate(Avg('value'))['value__avg'] or 0
            grade_count = subject_grades.count()
            change = - (100 - avg_grade) 
            subjects_data.append({
                'name': subject.name,
                'avg_grade': avg_grade,
                'grade_count': grade_count,
                'change': change
            })
        
        data = {
            'overall_performance': overall_performance,
            'total_grades': total_grades,
            'subjects_count': subjects_count,
            'subjects': subjects_data
        }
        serializer = JournalSummarySerializer(data)
        return Response(serializer.data)