from django.contrib import admin
from .models import URL, HealthCheck

@admin.register(URL)
class URLAdmin(admin.ModelAdmin):
    list_display = ['url', 'created_at']
    search_fields = ['url']

@admin.register(HealthCheck)
class HealthCheckAdmin(admin.ModelAdmin):
    list_display = ['url', 'status', 'response_time', 'checked_at']
    list_filter = ['status']
    search_fields = ['url__url']
