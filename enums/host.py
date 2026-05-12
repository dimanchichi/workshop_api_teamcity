from os import environ as env
from dotenv import load_dotenv

load_dotenv()

def _require_env(key: str) -> str:
    value = env.get(key)
    if not value:
        raise EnvironmentError(f"Required environment variable '{key}' is not set.")
    return value

USER = _require_env("TC_USER")
PASSWORD = _require_env("TC_PASSWORD")
BASE_URL = _require_env("TC_BASE_URL")