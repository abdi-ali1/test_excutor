from pathlib import Path
from typing import Dict, List, Any

class RobotTestBuilder:
    def build_from_json(self, config: Dict[str, Any]) -> Path:
        if "steps" not in config:
            raise ValueError("Missing 'steps' in test configuration.")

        robot_lines: List[str] = [
            "*** Settings ***",
            "Library    custom_energy_keywords.custom_validations",
            "Resource   ../resources/keywords.resource",
            "Library    RequestsLibrary",
  
            "*** Test Cases ***"
        ]

        test_name: str = config.get("name", "Generated Test")
        robot_lines.append(f"{test_name}")
        robot_lines.append("    [Tags]    contract    creation")  


        context = config.get("context")
        if context:
            context_dir = Path("generated_tests") / "context"
            context_dir.mkdir(parents=True, exist_ok=True)

            for key, value in context.items():
                filename = f"{key}.xml"
                path = context_dir / filename
                path.write_text(value, encoding="utf-8")
                print(f"[builder] Context file written: {path}")
                robot_lines.append(f"    Load XML File    ${{CURDIR}}/context/{filename}")


        steps: List[Dict[str, Any]] = config["steps"]
        for step in steps:
            keyword = step.get("keyword")
            args = step.get("args", [])
            args_line = "    ".join(args)

            if not keyword:
                raise ValueError("Each step must contain a 'keyword'.")

            robot_lines.append(f"    {keyword}    {args_line}")


        output_path = Path("generated_tests") / f"{test_name.replace(' ', '_')}.robot"
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text("\n".join(robot_lines), encoding="utf-8")

        return output_path
