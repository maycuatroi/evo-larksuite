import os

from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")

LARK_BASE_URL = "https://open.larksuite.com/open-apis/"
LARK_APP_ID = os.environ.get("LARK_APP_ID")
LARK_APP_SECRET = os.environ.get("LARK_APP_SECRET")
assert LARK_APP_ID is not None
