from api.auth_api import AuthAPI
from api.build_api import BuildAPI
from api.project_api import ProjectAPI


class ApiManager:
    def __init__(self, session):
        self.session = session
        self.auth_api = AuthAPI(session)
        self.project_api = ProjectAPI(session)
        self.build_config_api = BuildAPI(session)
