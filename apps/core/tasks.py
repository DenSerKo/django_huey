import logging
import time
from datetime import datetime

from django.utils import timezone
from huey import crontab
from huey.contrib.djhuey import periodic_task, task, db_task

from apps.core.models import DemoJob

logger = logging.getLogger(__name__)


@task(retries=3, retry_delay=10)
def send_test_notification(message):
    logger.info("Начинаем обработку уведомления: %s", message)
    logger.info("Уведомление обработано: %s", message)


@periodic_task(crontab(hour=8, minute=42))
def scheduled_test_task():
    logger.info("Периодическая задача выполнена: %s", datetime.now())


@db_task()
def run_demo_job(job_id):
    job = DemoJob.objects.get(pk=job_id)

    job.status = DemoJob.Status.RUNNING
    job.progress = 0
    job.save(update_fields=["status", "progress"])

    try:
        for step in range(1, 11):
            # Имитация выполнения части работы.
            time.sleep(3)

            # Увеличиваем прогресс на 10%.
            job.progress = step * 10
            job.save(update_fields=["progress"])

            logger.info(
                "Задача %s: прогресс %s%%",
                job.id,
                job.progress,
            )

        job.status = DemoJob.Status.SUCCESS
        job.result = "Задача успешно выполнена! Результат готов."

    except Exception as exc:
        job.status = DemoJob.Status.FAILED
        job.error = str(exc)
        raise

    finally:
        job.finished_at = timezone.now()
        job.save(
            update_fields=["status", "result", "error", "finished_at"]
        )
