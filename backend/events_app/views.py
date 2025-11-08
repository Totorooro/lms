from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import EventSerializer
from .models import Event


class EventViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]  