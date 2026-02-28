class BuildTypeData:
    @staticmethod
    def create_build_type_data(build_config_id):
        return {
            "buildType": {
                "id": build_config_id,
            }
        }