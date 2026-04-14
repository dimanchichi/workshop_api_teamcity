import os
from dotenv import load_dotenv

load_dotenv()

USER = os.getenv("TC_USER", "admin")
PASSWORD = os.getenv("TC_PASSWORD", "admin")
BASE_URL = os.getenv("TC_BASE_URL", "http://localhost:8111")