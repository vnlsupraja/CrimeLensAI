import os
from dotenv import load_dotenv

load_dotenv()

CATALYST_PROJECT_ID = os.getenv("CATALYST_PROJECT_ID")
CATALYST_CLIENT_ID = os.getenv("CATALYST_CLIENT_ID")
CATALYST_CLIENT_SECRET = os.getenv("CATALYST_CLIENT_SECRET")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")