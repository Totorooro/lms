from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Subject, Group, Lesson
from .serializers import SubjectSerializer, GroupSerializer, LessonSerializer
from datetime import datetime, timedelta


class SubjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [IsAuthenticated]


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]


class LessonViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        group = user.group  

        week_start = self.request.query_params.get('week_start')
        if week_start:
            start_date = datetime.strptime(week_start, '%Y-%m-%d').date()
        else:
            today = datetime.today().date()
            start_date = today - timedelta(days=today.weekday())  

        end_date = start_date + timedelta(days=6)
        weekday_start = start_date.weekday() + 1  
        weekday_end = end_date.weekday() + 1


        sept1 = datetime(2025, 9, 1).date()
        week_num = (start_date - sept1).days // 7 + 1  
        week_parity = 'even' if week_num % 2 == 0 else 'odd'

        queryset = Lesson.objects.filter(
            group=group,
            day__range=(weekday_start, weekday_end),
            week_type__in=['every', week_parity] 
        ).order_by('day', 'start_time')
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        grouped = {}
        for lesson in serializer.data:
            day = lesson['day']
            grouped.setdefault(day, []).append(lesson)
        return Response(grouped)
        