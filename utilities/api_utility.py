import requests
import time
from utilities.logger import get_logger

logger = get_logger(__name__)


class APIClient:

    def __init__(self, base_url, default_headers=None):
        self.base_url = base_url
        self.session = requests.Session()
        self.default_headers = default_headers or {}

    def _request(self, method, endpoint, **kwargs):
        url = f"{self.base_url}{endpoint}"

        headers = kwargs.pop("headers", {})
        merged_headers = {**self.default_headers, **headers}

        start_time = time.time()

        response = self.session.request(
            method=method,
            url=url,
            headers=merged_headers,
            **kwargs
        )

        response_time = round((time.time() - start_time) * 1000, 2)

        logger.info(f"{method} {url}")
        logger.info(f"Status Code: {response.status_code}")
        logger.info(f"Response Time: {response_time} ms")

        # Attach response_time to response object
        response.response_time_ms = response_time

        return response

    def get(self, endpoint, **kwargs):
        return self._request("GET", endpoint, **kwargs)

    def post(self, endpoint, **kwargs):
        return self._request("POST", endpoint, **kwargs)

    def put(self, endpoint, **kwargs):
        return self._request("PUT", endpoint, **kwargs)

    def delete(self, endpoint, **kwargs):
        return self._request("DELETE", endpoint, **kwargs)

    