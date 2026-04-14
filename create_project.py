import time

class TestProjectCreate:

    def test_create_project(self, api_manager, project_data, build_config_data, build_type_data):
        # Создание проекта
        create_project_response = api_manager.project_api.create_project(project_data).json()
        assert create_project_response.get("id") == project_data["id"]

        # Проверка проекта в списке
        get_project_response = api_manager.project_api.get_project().json()
        all_projects_ids = [project.get("id") for project in get_project_response.get("project", [])]
        assert project_data["id"] in all_projects_ids, "ID проекта не найден в списке существующих проектов"

        # Создание билд конфига
        api_manager.build_config_api.create_build_config(build_config_data)

        # Проверка билд конфига в списке
        get_build_config_response = api_manager.build_config_api.get_build_config_details().json()
        all_builds_ids = [build_type["id"] for build_type in get_build_config_response["buildType"]]
        assert build_config_data["id"] in all_builds_ids

        # Запуск билда
        start_build_response = api_manager.build_config_api.start_build_config(build_type_data).json()

        time.sleep(2)

        # Проверка запущенного билда
        get_started_build_response = api_manager.build_config_api.get_build_type_details().json()
        all_started_builds_ids = [build["buildTypeId"] for build in get_started_build_response["build"]]
        assert start_build_response["buildType"]["id"] in all_started_builds_ids

        # Очистка
        api_manager.build_config_api.clean_up_build_config(build_config_data["id"])
        api_manager.project_api.clean_up_project(project_data["id"])