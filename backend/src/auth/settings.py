import os
from dotenv import load_dotenv
load_dotenv()

DB_NAME = os.environ.get("DB_NAME")
AUTH0_DOMAIN = os.environ.get("AUTH0_DOMAIN")
ALGORITHMS = os.environ.get("ALGORITHMS")
API_AUDIENCE = os.environ.get("API_AUDIENCE")