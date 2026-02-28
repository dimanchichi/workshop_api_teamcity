from custom_requester.requester import CustomRequester


class AuthAPI(CustomRequester):
    """
    Класс отвечает за прохождение аутентификации путем получения токена и апдейта хэдеров
    """
    def __init__(self, session):
        super().__init__()
        self.session = session
        self.create_csrf_token()

    def create_csrf_token(self):
        self.session.auth = ("admin", "admin")
        csrf_token = self.send_request("GET", "/authenticationTest.html?csrf").text
        if not csrf_token:
            raise ValueError("CSRF token is missing")
        self._update_session_headers(**{"X-TC-CSRF-Token": csrf_token})