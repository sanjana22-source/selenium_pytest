class ResponseValidator:

    @staticmethod
    def validate_status_code(response, expected_status):
        actual_status = response.status_code
        assert actual_status == expected_status, (
            f"Expected status {expected_status}, "
            f"but got {actual_status}"
        )

    @staticmethod
    def validate_response_time(response, max_time_ms=2000):
        actual_time = response.response_time_ms
        assert actual_time <= max_time_ms, (
            f"Response time {actual_time}ms exceeded "
            f"maximum allowed {max_time_ms}ms"
        )

    @staticmethod
    def validate_json_response(response):
        try:
            response.json()
        except Exception:
            raise AssertionError("Response is not valid JSON")