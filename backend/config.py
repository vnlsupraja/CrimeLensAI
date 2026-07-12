import os
from dotenv import load_dotenv

load_dotenv()

CATALYST_PROJECT_ID = os.getenv("CATALYST_PROJECT_ID")
CATALYST_CLIENT_ID = os.getenv("CATALYST_CLIENT_ID")
CATALYST_CLIENT_SECRET = os.getenv("CATALYST_CLIENT_SECRET")
CATALYST_ENV = os.getenv("CATALYST_ENV", "Development")