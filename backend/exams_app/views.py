from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Exam
from .serializers import ExamSerializer

class ExamViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ExamSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Exam.objects.all().order_by('date', 'time')
