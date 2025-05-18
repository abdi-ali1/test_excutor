import os
import subprocess
from pathlib import Path
from typing import Dict


class RobotTestExecutor:
    def run_test(self, robot_file: Path) -> Dict[str, str]:
        if not robot_file.exists():
            raise FileNotFoundError(f"Test file not found: {robot_file}")

        # Bereken root pad naar project
        project_root = Path(__file__).resolve().parents[3]  # omhoog vanaf execution_runner

        env = os.environ.copy()
        env["PYTHONPATH"] = str(project_root / "libraries")

        result = subprocess.run(
            [
                "robot",
                "--outputdir", str(project_root / "results"),
                str(robot_file.resolve())
            ],
            capture_output=True,
            text=True,
            cwd=project_root,  # zodat relatieve imports kloppen
            env=env
        )

        return {
            "returncode": str(result.returncode),
            "stdout": result.stdout,
            "stderr": result.stderr
        }
