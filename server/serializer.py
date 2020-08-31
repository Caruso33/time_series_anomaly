from rest_framework import serializers
from .models import Zykluszeiten


class TimeSeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zykluszeiten
        fields = ['id', 'timestamp', 'cycle_time']
