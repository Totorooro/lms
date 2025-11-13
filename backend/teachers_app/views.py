from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Teacher
from .serializers import TeacherSerializer

class TeacherViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Получаем группу пользователя
        user_group = self.request.user.group if hasattr(self.request.user, 'group') and self.request.user.group else None
        if not user_group:
            return Teacher.objects.none()

        # Получаем имена преподавателей из Lesson для этой группы
        from schedule_app.models import Lesson
        teacher_names = Lesson.objects.filter(group=user_group).values_list('teacher', flat=True).distinct()
        
        # Фильтруем по полному совпадению имени
        return Teacher.objects.filter(full_name__in=teacher_names).order_by('full_name')