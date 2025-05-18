from robot.api.deco import keyword

class EnergyUtils:
    @keyword
    def validate_report_format(self, report):
        required_fields = ['total_consumption', 'peak_usage', 'period']
        for field in required_fields:
            if field not in report:
                raise AssertionError(f"Missing field: {field}")
        return True

    @keyword
    def validate_tariff_conditions(self, conditions):
        if not conditions:
            raise AssertionError("Tariff conditions are empty.")
        # Add more complex validation logic as needed
        return True
