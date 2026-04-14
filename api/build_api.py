from http import HTTPStatus

from custom_requester.requester import CustomRequester


class BuildAPI(CustomRequester):
    """
    Класс для работы с билдом
    """

    def __init__(self, session):
        super().__init__(session)

    def create_build_config(self, build_config_data, expected_status=HTTPStatus.INTERNAL_SERVER_ERROR):
        return self.send_request("POST", "/app/rest/buildTypes/", data=build_config_data, expected_status=expected_status)

    def get_build_config_details(self):
        return self.send_request("GET", f"/app/rest/buildTypes/")

    def start_build_config(self, build_type_data):
        return self.send_request("POST", "/app/rest/buildQueue/", data=build_type_data)

    def get_build_type_details(self):
        return self.send_request("GET", f"/app/rest/builds/")

    def delete_build_config(self, build_config_id, expected_status=HTTPStatus.NO_CONTENT):
        return self.send_request("DELETE", f"/app/rest/buildTypes/{build_config_id}", expected_status=expected_status)

    def clean_up_build_config(self, build_config_id):
        """
        Метод для проверки полного удаления билда
        """
        self.delete_build_config(build_config_id)
        get_build_config_response = self.get_build_config_details().json()
        all_configs_ids = [build.get("id", {}) for build in get_build_config_response.get("build", [])]
        assert build_config_id not in all_configs_ids, "ID удаленного билда найден в списке существующих билдов"