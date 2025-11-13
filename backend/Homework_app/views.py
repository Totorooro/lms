from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from .serializers import HomeworkSerializer
from .models import Homework

class HomeworkViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = HomeworkSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Homework.objects.all().order_by('-due_date')
        
        # Get user's group
        user_group = self.request.user.group if hasattr(self.request.user, 'group') and self.request.user.group else None
        
        if user_group:
            queryset = queryset.filter(group=user_group)
        
        # Update status for each homework
        for hw in queryset:
            hw.update_status()
        
        return queryset