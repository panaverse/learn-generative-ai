from starlette.config import Config
from starlette.datastructures import Secret

try:
    config = Config(".env")
except FileNotFoundError:
    config = Config()

OPENAI_API_KEY = config("OPENAI_API_KEY", cast=Secret)
