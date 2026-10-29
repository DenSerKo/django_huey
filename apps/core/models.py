from django.conf import settings
from django.db import models


class DemoJob(models.Model):
    class Status(models.TextChoices):
        PENDING = "pending", "Ожидает"
        RUNNING = "running", "Выполняется"
        SUCCESS = "success", "Завершено"
        FAILED = "failed", "Ошибка"

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING,
    )
    result = models.TextField(blank=True)
    error = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    finished_at = models.DateTimeField(null=True, blank=True)
    progress = models.PositiveSmallIntegerField(default=0)