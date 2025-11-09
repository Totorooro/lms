<<<<<<< HEAD
from django.shortcuts import render

# Create your views here.
=======
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from .serializers import EventSerializer
from .models import Event

class EventViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Event.objects.all().order_by('-start_date')
        
        user_group = self.request.user.group if hasattr(self.request.user, 'group') and self.request.user.group else None
        
        if user_group:
            queryset = queryset.filter(Q(groups__pk__isnull=True) | Q(groups=user_group)).distinct()
        else:
            queryset = queryset.filter(groups__pk__isnull=True)
        
        for event in queryset:
            event.update_status()
        
        return queryset

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

    @action(detail=True, methods=['post'])
    def register(self, request, pk=None):
        event = self.get_object()
        user = request.user
        
        if event.participants_limit > 0 and event.current_participants >= event.participants_limit:
            return Response({'detail': 'Места закончились'}, status=status.HTTP_400_BAD_REQUEST)
        
        if event.participants.filter(id=user.id).exists():
            return Response({'detail': 'Вы уже зарегистрированы'}, status=status.HTTP_400_BAD_REQUEST)
        
        event.participants.add(user)
        event.current_participants += 1
        event.save()
        
        return Response({'detail': 'Успешно зарегистрировано'})
>>>>>>> 9df53b4cc22ac6cf660fc88c39f35d33284bf285
