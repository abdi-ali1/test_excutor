from pydantic import BaseModel
from typing import List, Dict, Any, Optional


class StepModel(BaseModel):
    keyword: str
    args: List[str]


class JsonConfig(BaseModel):
    name: str
    steps: List[StepModel]
    context: Optional[Dict[str, Any]] = None  


class ExecutionRequest(BaseModel):
    json_config: JsonConfig
