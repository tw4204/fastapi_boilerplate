from alembic.config import Config
from alembic import command
import os
from setting import Setting
base_path = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(base_path, 'database', 'alembic.ini')
alembic_cfg = Config(config_path)

setting = Setting()
alembic_cfg.set_main_option("sqlalchemy.url", setting.SQLALCHEMY_DATABASE_URL)

if __name__ == '__main__':
    command.revision(alembic_cfg, autogenerate=True)
    command.upgrade(alembic_cfg, "head")
