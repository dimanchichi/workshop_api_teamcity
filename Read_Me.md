
## Getting Started

This project - about how to make an API autotests for TeamCity CI/CD


### Components

* Create_project - contains test for API
* gitignore - must have
* enums - for vars
* custom_requester - враппер для отправки запросов (сюда кидаем базовые хэдеры, метод отправки запроса, метод дополнения хэдеров)
* utils - директория для хранения утилит (ех - генерация даты)
* -- data_generator - генерация данных с использованием Faker
* data_for_test - директория формирования тестовых данных
* -- project_data - генерация даты с помощью дата_генератора для создания проекта