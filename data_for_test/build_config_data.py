from utils.data_generator import DataGenerator


class BuildConfigData:
    @staticmethod
    def create_build_config_data(last_project_id):
        return {
            "id": DataGenerator.generate_build_config_id(),
            "name": DataGenerator.generate_build_config_name(),
            "project": {
                "id": last_project_id
            },
            "templates": {
                "buildType": []
            },
            "vcs-root-entries": {
                "count": 1,
                "vcs-root-entry": [
                    {
                        "id": "SpringCoreForQa_HttpsGithubComAlexPsheSpringCoreForQaRefsHeadsMaster",
                        "vcs-root": {
                            "id": "SpringCoreForQa_HttpsGithubComAlexPsheSpringCoreForQaRefsHeadsMaster",
                            "name": "https://github.com/AlexPshe/spring-core-for-qa#refs/heads/master",
                            "href": "/app/rest/vcs-roots/id:SpringCoreForQa_HttpsGithubComAlexPsheSpringCoreForQaRefsHeadsMaster"
                        },
                        "checkout-rules": ""
                    }
                ]
            },
            "settings": {
                "property": [
                    {
                        "name": "buildNumberCounter",
                        "value": "4"
                    }
                ],
                "count": 1
            },
            "parameters": {
                "property": [],
                "count": 0
            },
            "output-parameters": {
                "property": [],
                "count": 0
            },
            "steps": {
                "step": [
                    {
                        "id": "Print_Hello_World_auto",
                        "name": "Print Hello World auto",
                        "type": "simpleRunner",
                        "properties": {
                            "property": [
                                {
                                    "name": "script.content",
                                    "value": "echo \"Hello, world!\""
                                },
                                {
                                    "name": "teamcity.step.mode",
                                    "value": "default"
                                },
                                {
                                    "name": "use.custom.script",
                                    "value": "true"
                                }
                            ],
                            "count": 3
                        }
                    }
                ]
            },
            "features": {
                "count": 1,
                "feature": [
                    {
                        "id": "perfmon",
                        "type": "perfmon",
                        "properties": {
                            "property": [
                                {
                                    "name": "teamcity.perfmon.feature.enabled",
                                    "value": "true"
                                }
                            ],
                            "count": 1
                        }
                    }
                ]
            },
            "triggers": {
                "count": 1,
                "trigger": [
                    {
                        "id": "TRIGGER_1",
                        "type": "vcsTrigger",
                        "properties": {
                            "property": [
                                {
                                    "name": "branchFilter",
                                    "value": "+:*"
                                },
                                {
                                    "name": "enableQueueOptimization",
                                    "value": "true"
                                },
                                {
                                    "name": "quietPeriodMode",
                                    "value": "DO_NOT_USE"
                                }
                            ],
                            "count": 3
                        }
                    }
                ]
            },
            "snapshot-dependencies": {
                "count": 0
            },
            "artifact-dependencies": {
                "count": 0
            },
            "agent-requirements": {
                "count": 0
            },
            "builds": {},
            "investigations": {},
            "compatibleAgents": {},
            "compatibleCloudImages": {}
        }