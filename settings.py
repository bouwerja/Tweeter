from dotenv import load_dotenv
import os

load_dotenv()

API = os.getenv("API_KEY")
API_SECRET = os.getenv("API_KEY_SECRET")

ACCESS = os.getenv("ACCESS_TOKEN")
ACCESS_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

OAUTH2_ACCESS_TOKEN = os.getenv("OAUTH")

BEARER_TOKEN = os.getenv("BEARER")