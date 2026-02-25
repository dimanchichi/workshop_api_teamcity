from http import HTTPStatus

import requests
from pprint import pprint

from data_for_test.project_data import ProjectData
from custom_requester.requester import CustomRequester

class TestProjectCreate:

    @classmethod
    def setup_class(cls):
        cls.project_data = ProjectData.create_project_data()
        cls.project_id = cls.project_data["id"]

    def test_create_project(self):
        requester = CustomRequester(requests.Session())
        requester.session.auth = ("admin", "admin")

        csrf_token = requester.send_request("GET", "/authenticationTest.html?csrf").text
        requester._update_session_headers(**{"X-TC-CSRF-Token": csrf_token})

        requester.send_request("POST", "/app/rest/projects", data=self.project_data)

        requester.send_request("GET", f"/app/rest/projects/{self.project_id}")

        # json_for_new_build_config = {
        #     "id": "BuildConfbyAuto",
        #     "name": "Build Conf by Auto",
        #     "project": {
        #         "id": last_project_id
        #     },
        #     "templates": {
        #         "buildType": []
        #     },
        #     "vcs-root-entries": {
        #         "count": 1,
        #         "vcs-root-entry": [
        #             {
        #                 "id": "SpringCoreForQa_HttpsGithubComAlexPsheSpringCoreForQaRefsHeadsMaster",
        #                 "vcs-root": {
        #                     "id": "SpringCoreForQa_HttpsGithubComAlexPsheSpringCoreForQaRefsHeadsMaster",
        #                     "name": "https://github.com/AlexPshe/spring-core-for-qa#refs/heads/master",
        #                     "href": "/app/rest/vcs-roots/id:SpringCoreForQa_HttpsGithubComAlexPsheSpringCoreForQaRefsHeadsMaster"
        #                 },
        #                 "checkout-rules": ""
        #             }
        #         ]
        #     },
        #     "settings": {
        #         "property": [
        #             {
        #                 "name": "buildNumberCounter",
        #                 "value": "4"
        #             }
        #         ],
        #         "count": 1
        #     },
        #     "parameters": {
        #         "property": [],
        #         "count": 0
        #     },
        #     "output-parameters": {
        #         "property": [],
        #         "count": 0
        #     },
        #     "steps": {
        #         "step": [
        #             {
        #                 "id": "Print_Hello_World_auto",
        #                 "name": "Print Hello World auto",
        #                 "type": "simpleRunner",
        #                 "properties": {
        #                     "property": [
        #                         {
        #                             "name": "script.content",
        #                             "value": "echo \"Hello, world!\""
        #                         },
        #                         {
        #                             "name": "teamcity.step.mode",
        #                             "value": "default"
        #                         },
        #                         {
        #                             "name": "use.custom.script",
        #                             "value": "true"
        #                         }
        #                     ],
        #                     "count": 3
        #                 }
        #             }
        #         ]
        #     },
        #     "features": {
        #         "count": 1,
        #         "feature": [
        #             {
        #                 "id": "perfmon",
        #                 "type": "perfmon",
        #                 "properties": {
        #                     "property": [
        #                         {
        #                             "name": "teamcity.perfmon.feature.enabled",
        #                             "value": "true"
        #                         }
        #                     ],
        #                     "count": 1
        #                 }
        #             }
        #         ]
        #     },
        #     "triggers": {
        #         "count": 1,
        #         "trigger": [
        #             {
        #                 "id": "TRIGGER_1",
        #                 "type": "vcsTrigger",
        #                 "properties": {
        #                     "property": [
        #                         {
        #                             "name": "branchFilter",
        #                             "value": "+:*"
        #                         },
        #                         {
        #                             "name": "enableQueueOptimization",
        #                             "value": "true"
        #                         },
        #                         {
        #                             "name": "quietPeriodMode",
        #                             "value": "DO_NOT_USE"
        #                         }
        #                     ],
        #                     "count": 3
        #                 }
        #             }
        #         ]
        #     },
        #     "snapshot-dependencies": {
        #         "count": 0
        #     },
        #     "artifact-dependencies": {
        #         "count": 0
        #     },
        #     "agent-requirements": {
        #         "count": 0
        #     },
        #     "builds": {},
        #     "investigations": {},
        #     "compatibleAgents": {},
        #     "compatibleCloudImages": {}
        # }
        #
        # requests.post(
        #     url=BASE_URL + "/app/rest/buildTypes",
        #     headers=headers,
        #     json=json_for_new_build_config
        # )
        #
        # check_build_config = requests.get(url=BASE_URL + "/app/rest/buildTypes/BuildConfbyAuto", headers=headers)
        # assert check_build_config.status_code == 200, f"Build config is not present: {check_build_config.text}"
        # last_build_config_id = check_build_config.json()["id"]
        #
        # json_for_start_build = {
        #     "buildType": {
        #         "id": last_build_config_id
        #     }
        # }
        #
        # start_build = requests.post(
        #     url=BASE_URL + "/app/rest/buildQueue",
        #     headers=headers,
        #     json=json_for_start_build
        # )
        # assert start_build.status_code == 200, f"Build not started: {start_build.text}"
        # build_id = start_build.json()["id"]
        #
        # get_starting_build_details = requests.get(url= BASE_URL + f"/app/rest/builds/{build_id}", headers=headers)
        # assert get_starting_build_details.status_code == 200, f"Build details is not present: {get_starting_build_details.text}"
        #
        # delete_build_config = requests.delete(url=BASE_URL + f"/app/rest/buildTypes/{last_build_config_id}", headers=headers)
        # assert delete_build_config.status_code == 204, f"Build config is not present: {delete_build_config.text}"
        #
        # check_build_config = requests.get(url=BASE_URL + "/app/rest/buildTypes/BuildConfbyAuto", headers=headers)
        # assert check_build_config.status_code == 404, f"Build config is not deleted: {check_build_config.text}"

        requester.send_request("DELETE", f"/app/rest/projects/{self.project_id}", expected_status=HTTPStatus.NO_CONTENT)

        requester.send_request("GET", f"/app/rest/projects/{self.project_id}", expected_status=HTTPStatus.NOT_FOUND)
