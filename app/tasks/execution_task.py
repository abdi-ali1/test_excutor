from celery_app import celery
from app.services.execution_runner.runner import ExecutionRunner


@celery.task
def run_test_task(payload: dict) -> dict:
    print(f"[Celery] Running test with payload: {payload}")
    return ExecutionRunner().run(payload)



