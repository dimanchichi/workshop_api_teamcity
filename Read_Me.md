
## Getting Started

This project - about how to make an API autotests for TeamCity CI/CD


### Components

* Create_project - contains test for API
* gitignore - must have
* enums - for vars
* custom_requester - враппер для отправки запросов (сюда кидаем базовые хэдеры, метод отправки запроса, метод дополнения хэдеров)
* utils - директория для хранения утилит (ех - генерация даты)
* -- data_generator - генерация данных с использованием Faker