import os
from pydantic import (
    BaseSettings,
    PostgresDsn
)
class Setting(BaseSettings):
    DATABASE_USER: str = os.environ['DATABASE_USER']
    DATABASE_PASS: str = os.environ['DATABASE_PASS']
    DATABASE_SERVICE: str = os.environ['DATABASE_SERVICE']
    DATABASE_PORT: str = os.environ['DATABASE_PORT']
    DATABASE_NAME: str = os.environ['DATABASE_NAME']
    SQLALCHEMY_DATABASE_URL: PostgresDsn = (
        'postgresql://'
        f'{DATABASE_USER}:{DATABASE_PASS}@'
        f'{DATABASE_SERVICE}:{DATABASE_PORT}'
        f'/{DATABASE_NAME}'
    )
