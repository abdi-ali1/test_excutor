from fastapi import APIRouter, status
from app.models.execution_model import ExecutionRequest
from app.tasks.execution_task import run_test_task

router = APIRouter()

@router.post("", status_code=status.HTTP_202_ACCEPTED)
def run_execution(request: ExecutionRequest) -> dict:
    run_test_task.delay(request.model_dump())
    return {"message": "Test scheduled"}
