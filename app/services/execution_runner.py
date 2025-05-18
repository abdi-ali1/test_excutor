from typing import Dict


class ExecutionRunner:
    def run(self, payload: Dict[str, str]) -> dict:
        return {"status": "completed", "name": payload.get("name")}
