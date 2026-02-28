from http import HTTPStatus

import requests
from pprint import pprint

from custom_requester import requester
from data_for_test.build_config_data import BuildConfigData
from data_for_test.build_type_data import BuildTypeData
from data_for_test.project_data import ProjectData
from custom_requester.requester import CustomRequester

class TestProjectCreate:

    @classmethod
    def setup_class(cls):
        cls.project_data = ProjectData.create_project_data()
        cls.project_id = cls.project_data["id"]
        cls.build_config_data = BuildConfigData.create_build_config_data(cls.project_id)
        cls.build_config_id = cls.build_config_data["id"]
        cls.build_type_data = BuildTypeData.create_build_type_data(cls.build_config_id)

    def test_create_project(self):
        requester = CustomRequester(requests.Session())
        requester.session.auth = ("admin", "admin")

        csrf_token = requester.send_request("GET", "/authenticationTest.html?csrf").text
        requester._update_session_headers(**{"X-TC-CSRF-Token": csrf_token})

        requester.send_request("POST", "/app/rest/projects", data=self.project_data)

        requester.send_request("GET", f"/app/rest/projects/{self.project_id}")

        requester.send_request("POST", "/app/rest/buildTypes", data=self.build_config_data, expected_status=HTTPStatus.INTERNAL_SERVER_ERROR)

        requester.send_request("GET", f"/app/rest/buildTypes/{self.build_config_id}")

        started_build_id = requester.send_request("POST", f"/app/rest/buildQueue", data=self.build_type_data).json()["id"]

        requester.send_request("GET", f"/app/rest/builds/{started_build_id}")

        requester.send_request("DELETE", f"/app/rest/buildTypes/{self.build_config_id}", expected_status=HTTPStatus.NO_CONTENT)

        requester.send_request("GET", f"/app/rest/buildTypes/{self.build_config_id}", expected_status=HTTPStatus.NOT_FOUND)

        requester.send_request("DELETE", f"/app/rest/projects/{self.project_id}", expected_status=HTTPStatus.NO_CONTENT)

        requester.send_request("GET", f"/app/rest/projects/{self.project_id}", expected_status=HTTPStatus.NOT_FOUND)
