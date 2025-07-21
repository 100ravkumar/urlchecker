from django.db import models

class URL(models.Model):
    url = models.URLField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.url

class HealthCheck(models.Model):
    url = models.ForeignKey(URL, on_delete=models.CASCADE, related_name='checks')
    status = models.CharField(max_length=10)  # up/down
    response_time = models.FloatField()  # in seconds
    checked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.url} - {self.status} @ {self.checked_at}"
