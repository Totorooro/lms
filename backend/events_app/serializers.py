from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.ModelSerializer):
    progress = serializers.ReadOnlyField()
    
    class Meta:
        model = Event
        fields = '__all__'