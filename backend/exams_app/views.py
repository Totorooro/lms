from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Exam
from .serializers import ExamSerializer

class ExamViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ExamSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_group = self.request.user.group if hasattr(self.request.user, 'group') and self.request.user.group else None
        if not user_group:
            return Exam.objects.none()
        return Exam.objects.filter(group=user_group).order_by('date', 'time')