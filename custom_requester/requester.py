import logging
import os
from http import HTTPStatus
from typing import Optional, Any, Dict

from enums.host import BASE_URL

class CustomRequester:
    def __init__(self, session = None):
        self.session = session
        self.base_url = BASE_URL
        self.logger = logging.getLogger(__name__)
        self.base_headers = dict({
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        })
        self._update_session_headers()

    def send_request(self, method: str,
                     endpoint: str,
                     data: Optional[Dict[str, Any]] = None,
                     expected_status: HTTPStatus = HTTPStatus.OK,
                     need_logging = True):
        """
        Враппер для запросов
        :param method: метод запроса
        :param endpoint: эндпоинт для склейки с base_url
        :param data: тело запроса - по умолчанию пустое
        :param expected_status: ожидаемый статус код
        :return: возвращает объект ответа
        """
        url = f"{self.base_url}{endpoint}"
        response = self.session.request(method=method.upper(), url=url, json=data)
        if need_logging:
            self.log_request_and_response(response)
        if response.status_code != expected_status.value:
            raise ValueError(f"Unexpected status code: {response.status_code}. Expected: {expected_status.value}")
        return response

    def _update_session_headers(self, **kwargs):
        self.headers = self.base_headers.copy()
        self.headers.update(kwargs)
        self.session.headers.update(self.headers)

    def log_request_and_response(self, response):
        try:
            request = response.request
            GREEN = "\033[92m"
            RED = "\033[91m"
            RESET = "\033[0m"
            SENSITIVE = {"Authorization", "Cookie"}

            headers = " \\\n".join([
                f"-H '{k}: {'***' if k in SENSITIVE else v}'"
                for k, v in request.headers.items()
            ])
            full_test_name = f"pytest {os.environ.get('PYTEST_CURRENT_TEST', '').replace('(call)', '')}"

            body = ""
            if hasattr(request, "body") and request.body is not None:
                if isinstance(request.body, bytes):
                    body = request.body.decode("utf-8", errors="replace")
                elif isinstance(request.body, str):
                    body = request.body
            body_part = f"-d '{body}' \\\n" if body and body != '{}' else ""

            self.logger.info(
                f"{GREEN}{full_test_name}{RESET}\n"
                f"curl -X {request.method} '{request.url}' \\\n"
                f"{headers} \\\n"
                f"{body_part}"
            )

            color = RESET if response.ok else RED
            self.logger.info(
                f"\nRESPONSE:"
                f"\nSTATUS_CODE: {color}{response.status_code}{RESET}"
                f"\nDATA: {color}{response.text}{RESET}"
            )

        except Exception as e:
            self.logger.info(f"\nLogging went wrong: {type(e)} - {e}")