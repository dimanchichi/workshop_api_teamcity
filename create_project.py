import time

from data_for_test.build_config_data import BuildConfigData
from data_for_test.build_type_data import BuildTypeData
from data_for_test.project_data import ProjectData

class TestProjectCreate:

    @classmethod
    def setup_class(cls):
        cls.project_data = ProjectData.create_project_data()
        cls.project_id = cls.project_data["id"]
        cls.build_config_data = BuildConfigData.create_build_config_data(cls.project_id)
        cls.build_config_id = cls.build_config_data["id"]
        cls.build_type_data = BuildTypeData.create_build_type_data(cls.build_config_id)
        cls.build_type_data_id = cls.build_type_data["buildType"]["id"]

    def test_create_project(self, api_manager):
        create_project_response = api_manager.project_api.create_project(self.project_data).json()
        assert create_project_response.get("id") == self.project_id

        get_project_response = api_manager.project_api.get_project().json()
        all_projects_ids = [project.get("id", {}) for project in get_project_response.get("project", [])]
        assert self.project_id in all_projects_ids, "ID проекта не найден в списке существующих проектов"

        api_manager.build_config_api.create_build_config(self.build_config_data)

        get_build_config_response = api_manager.build_config_api.get_build_config_details().json()
        all_builds_ids = [build_type["id"] for build_type in get_build_config_response["buildType"]]
        assert self.build_config_id in all_builds_ids

        start_build_response = api_manager.build_config_api.start_build_config(self.build_type_data).json()

        time.sleep(2)

        get_started_build_response = api_manager.build_config_api.get_build_type_details().json()
        all_started_builds_ids = [build["buildTypeId"] for build in get_started_build_response["build"]]
        assert start_build_response["buildType"]["id"] in all_started_builds_ids

        api_manager.build_config_api.clean_up_build_config(self.build_config_id)

        api_manager.project_api.clean_up_project(self.project_id)