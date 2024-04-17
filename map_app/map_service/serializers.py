from rest_framework import serializers
from .models import Seats

class SeatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seats
        fields = ('seat_number', 'is_occupied')