from http import HTTPStatus

from custom_requester.requester import CustomRequester


class ProjectAPI(CustomRequester):
    """
    Класс для работы с проектом
    """

    def create_project(self, project_data):
        return self.send_request("POST", "/app/rest/projects", data=project_data)

    def get_project(self):
        return self.send_request("GET", f"/app/rest/projects/")

    def delete_project(self, project_id, expected_status=HTTPStatus.NO_CONTENT):
        return self.send_request("DELETE", f"/app/rest/projects/id:{project_id}", expected_status=expected_status)

    def clean_up_project(self, project_id):
        """
        Метод для проверки полного удаления проекта
        """
        self.delete_project(project_id)
        get_project_response = self.get_project().json()
        all_projects_ids = [project.get("id", {}) for project in get_project_response.get("project", [])]
        assert project_id not in all_projects_ids, "ID удаленного проекта найден в списке существующих проектов"
