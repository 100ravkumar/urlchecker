# monitor/views.py

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import URL, HealthCheck
from .serializers import URLSerializer, HealthCheckSerializer
from .tasks import check_url_health

from django_celery_beat.models import PeriodicTask, IntervalSchedule
import json

class URLCreateAPIView(generics.CreateAPIView):
    queryset = URL.objects.all()
    serializer_class = URLSerializer

    def perform_create(self, serializer):
        url = serializer.save()

        # Create or get 5-minute interval
        schedule, created = IntervalSchedule.objects.get_or_create(
            every=5,
            period=IntervalSchedule.MINUTES,
        )

        # Add periodic task for this URL
        PeriodicTask.objects.create(
            interval=schedule,
            name=f"Health Check for URL {url.id}",
            task='monitor.tasks.check_url_health',
            args=json.dumps([url.id]),
        )


class HealthCheckListAPIView(generics.ListAPIView):
    serializer_class = HealthCheckSerializer

    def get_queryset(self):
        url_id = self.kwargs['pk']
        return HealthCheck.objects.filter(url_id=url_id).order_by('-checked_at')[:5]
