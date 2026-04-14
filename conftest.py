import pytest
import requests

from api.api_manager import ApiManager
from data_for_test.project_data import ProjectData
from data_for_test.build_config_data import BuildConfigData
from data_for_test.build_type_data import BuildTypeData

from enums.host import USER, PASSWORD, BASE_URL


@pytest.fixture
def session():
    """
    Создание сессии и передача ее в тесты
    """
    http_session = requests.Session()
    http_session.auth = (USER, PASSWORD)

    csrf_token = http_session.get(f"{BASE_URL}/authenticationTest.html?csrf").text.strip()
    http_session.headers.update({"X-TC-CSRF-Token": csrf_token})

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

@pytest.fixture
def project_data():
    return ProjectData.create_project_data()

@pytest.fixture
def build_config_data(project_data):
    return BuildConfigData.create_build_config_data(project_data["id"])

@pytest.fixture
def build_type_data(build_config_data):
    return BuildTypeData.create_build_type_data(build_config_data["id"])