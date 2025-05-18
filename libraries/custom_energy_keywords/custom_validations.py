from robot.api.deco import keyword
from pathlib import Path
import xmlschema
import sys
from pathlib import Path


project_root = Path(__file__).resolve().parents[2]  
libraries_path = project_root / "libraries"
if str(libraries_path) not in sys.path:
    sys.path.insert(0, str(libraries_path))


@keyword("Get File From Library")
def get_file(filepath):
    file_path = Path(filepath)
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {filepath}")
    return file_path.read_text(encoding="utf-8")

@keyword("Validate Response Status From Library")
def validate_response_status(expected_status: int):
    from robot.libraries.BuiltIn import BuiltIn
    actual_status = BuiltIn().get_variable_value("${response_status}")
    if actual_status != expected_status:
        raise AssertionError(f"Expected status {expected_status}, got {actual_status}")

@keyword("Validate XML Schema From Library")
def validate_xml_schema(xml_string: str, xsd_file: str):
    schema = xmlschema.XMLSchema(xsd_file)
    if not schema.is_valid(xml_string):
        raise AssertionError("XML does not conform to schema.")
