from starlette.config import Config

try:
    config = Config(".env")
except FileNotFoundError:
    config = Config()

KONG_ADMIN_URL = config("KONG_ADMIN_URL", cast=str)
