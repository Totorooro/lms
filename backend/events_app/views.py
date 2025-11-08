from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import EventSerializer
from .models import Event
from django.db.models import Q


class EventViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]  

    def get_queryset(self):
        queryset = Event.objects.all().order_by('-start_date')
        
        user_group = self.request.user.group if hasattr(self.request.user, 'group') and self.request.user.group else None
        
        if user_group:
            queryset = queryset.filter(Q(groups__isnull=True) | Q(groups=user_group)).distinct()
        else:
            queryset = queryset.filter(groups__isnull=True)
        

        for event in queryset:
            event.update_status()
        
        return queryset
