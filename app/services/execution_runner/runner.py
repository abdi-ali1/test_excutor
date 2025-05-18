from typing import Dict, Any

from app.services.execution_runner.builder import RobotTestBuilder
from app.services.execution_runner.executor import RobotTestExecutor


class ExecutionRunner:
    def run(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        print("[ExecutionRunner] Building Robot Framework test...")
        test_file = RobotTestBuilder().build_from_json(payload["json_config"])

        print(f"[ExecutionRunner] Test generated at: {test_file}")

        result = RobotTestExecutor().run_test(test_file)

        print(f"[ExecutionRunner] Test execution complete. Return code: {result['returncode']}")

        return {
            "test_file": str(test_file),
            "result": result
        }
