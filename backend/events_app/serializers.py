from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.ModelSerializer):
    progress = serializers.ReadOnlyField()
    is_registered = serializers.SerializerMethodField()
    
    class Meta:
        model = Event
        fields = '__all__'
    

    def get_is_registered(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            return obj.participants.filter(id=user.id).exists()
        return False