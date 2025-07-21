# monitor/tasks.py

import requests
from celery import shared_task
from .models import URL, HealthCheck

@shared_task
def check_url_health(url_id):
    try:
        url_obj = URL.objects.get(id=url_id)
        response = requests.get(url_obj.url, timeout=5)
        status = 'up' if response.status_code == 200 else 'down'
        response_time = response.elapsed.total_seconds()
    except Exception as e:
        status = 'down'
        response_time = 0.0

    HealthCheck.objects.create(
        url_id=url_id,
        status=status,
        response_time=response_time
    )
