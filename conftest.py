import pytest
import requests

from api.api_manager import ApiManager


@pytest.fixture
def session():
    """
    Создание сессии
    """
    http_session = requests.Session()
    yield http_session

    http_session.close()

@pytest.fixture
def api_manager(session):
    """
    Обогащение и создание ApiManager c session
    :param session:
    :return:
    """
    return ApiManager(session)