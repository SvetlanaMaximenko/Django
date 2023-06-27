from rest_framework import serializers
from .models import Event, User


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"
        read_only_fields = ["name", "meeting_time", "description"]

    def to_representation(self, instance: Event):
        result: dict = super().to_representation(instance)
        return result


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username"]

