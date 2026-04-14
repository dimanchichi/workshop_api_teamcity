# TeamCity API Autotests

Фреймворк для автоматизированного тестирования REST API TeamCity CI/CD.

## Стек

- **Python** 3.11.9
- **pytest** — тест-раннер
- **requests** — HTTP-клиент
- **Faker** — генерация тестовых данных
- **python-dotenv** — управление конфигурацией

## Требования

- Python 3.11.9
- Docker и Docker Compose

## Быстрый старт

### 1. Клонировать репозиторий

```bash
git clone https://github.com/dimanchichi/workshop_api_teamcity.git
cd workshop_api_teamcity
```

### 2. Запустить TeamCity в Docker

```bash
docker compose up -d
```

Дождаться запуска сервера и агента. TeamCity будет доступен по адресу `http://localhost:8111`.  
При первом запуске пройти начальную настройку через браузер и создать администратора.

### 3. Установить зависимости

```bash
pip install -r requirements
```

### 4. Настроить переменные окружения

Скопировать `.env.copy` и переименовать в `.env`:

```bash
cp .env.copy .env
```

Открыть `.env` и заполнить своими значениями:

```env
TC_USER=your_admin_username
TC_PASSWORD=your_admin_password
TC_BASE_URL=http://localhost:8111
```

## Структура проекта

```
├── api/                        # API-клиенты
│   ├── api_manager.py          # Точка входа, объединяет все API-клиенты
│   ├── auth_api.py             # Аутентификация
│   ├── project_api.py          # Работа с проектами (создание/удаление)
│   ├── build_api.py            # Работа с билдами (создание/запуск/удаление)
│   └── user_api.py             # Работа с пользователями
│
├── custom_requester/
│   └── requester.py            # Базовый HTTP-клиент с логированием
│
├── data_for_test/              # Генерация тестовых данных
│   ├── project_data.py         # Данные для создания проекта
│   ├── build_config_data.py    # Данные для создания билд-конфига
│   └── build_type_data.py      # Данные для запуска билда
│
├── enums/
│   └── host.py                 # Конфигурация подключения (из .env)
│
├── utils/
│   └── data_generator.py       # Генерация случайных данных через Faker
│
├── conftest.py                 # Фикстуры pytest (сессия, api_manager, тестовые данные)
├── create_project.py           # Тесты: создание проекта и запуск билда
├── pytest.ini                  # Конфигурация pytest и логгера
├── .env                        # Локальные переменные окружения (не в git)
├── .env.copy                   # Шаблон переменных окружения (в git)
├── .gitignore
└── requirements                # Зависимости проекта
```

## Архитектура

```
conftest.py (фикстуры)
    └── ApiManager
            ├── ProjectAPI  ──┐
            ├── BuildAPI    ──┤──► CustomRequester (отправка запросов + логирование)
            ├── AuthAPI     ──┤
            └── UserAPI     ──┘
```

Каждый API-класс наследует `CustomRequester` и использует метод `send_request` для отправки запросов. Все запросы автоматически логируются в формате `curl`-команды для удобного воспроизведения вручную.

## Логирование

Каждый запрос и ответ логируется в формате:

```
pytest create_project.py::TestProjectCreate::test_create_project
curl -X POST 'http://localhost:8111/app/rest/projects' \
-H 'Accept: application/json' \
-H 'Authorization: ***' \
-d '{"name": "example", "id": "abc123", ...}'

RESPONSE:
STATUS_CODE: 200
DATA: {"id":"abc123", ...}
```

Чувствительные заголовки (`Authorization`, `Cookie`) маскируются автоматически.

## Конфигурация pytest

Настройки в `pytest.ini`:

```ini
[pytest]
log_cli = true
log_cli_level = INFO
log_cli_format = %(asctime)s %(levelname)s %(message)s
log_cli_date_format = %Y-%m-%d %H:%M:%S
```