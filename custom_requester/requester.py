from http import HTTPStatus
from typing import Optional, Any, Dict

from enums.host import BASE_URL

class CustomRequester:
    base_headers = dict({
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    })

    def __init__(self, session):
        self.session = session
        self.base_url = BASE_URL

    def send_request(self, method: str, endpoint: str, data: Optional[Dict[str, Any]] = None, expected_status: HTTPStatus = HTTPStatus.OK):
        """
        Враппер для запросов
        :param method: метод запроса
        :param endpoint: эндпоинт для склейки с base_url
        :param data: тело запроса - по умолчанию пустое
        :param expected_status: ожидаемый статус код
        :return: возвращает объект ответа
        """
        url = f"{self.base_url}{endpoint}"
        response = self.session.request(method, url, json=data)
        if response.status_code != expected_status:
            raise ValueError(f"Unexpected status code: {response.status_code}")
        return response

    def _update_session_headers(self, **kwargs):
        self.headers=self.base_headers.copy()
        self.headers.update(kwargs)
        self.session.headers.update(self.headers)

        

