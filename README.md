
## Getting Started

This project - about how to make an API autotests for TeamCity CI/CD


### Components

* Create_project - contains test for API
* gitignore - must have
* enums - for vars
* -- host - для хранения хоста
* custom_requester - враппер для отправки запросов (сюда кидаем базовые хэдеры, метод отправки запроса, метод дополнения хэдеров) и логирование
* utils - директория для хранения утилит (ех - генерация даты)
* -- data_generator - генерация данных с использованием Faker
* data_for_test - директория формирования тестовых данных
* -- project_data - генерация даты для создания проектас помощью дата_генератора для создания проекта
* -- build_config_data - генерация даты для создания билда
* -- build_type_data - генерация даты для запуска билда
* pytest.ini - конфигурации, настройки логера
* api 
* -- auth_api - класс для прохождения аутентификации
* -- project_api - класс для работы с проектом (создание/удаление)
* -- api_manager - управление API
* conftest.py - хранение фикстур (создание session и обогащение им api manager)