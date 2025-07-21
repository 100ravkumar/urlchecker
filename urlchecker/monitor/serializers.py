# monitor/serializers.py

from rest_framework import serializers
from .models import URL, HealthCheck

class URLSerializer(serializers.ModelSerializer):
    class Meta:
        model = URL
        fields = ['id', 'url', 'created_at']

class HealthCheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthCheck
        fields = ['status', 'response_time', 'checked_at']
