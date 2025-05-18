from celery import Celery
from app.config.settings import settings

celery = Celery(
    "test_executor",
    broker=settings.redis_broker_url,
    backend=settings.redis_result_backend
)

celery.conf.task_routes = {
    "app.tasks.*": {"queue": "test-queue"}
}

from app.tasks import execution_task
