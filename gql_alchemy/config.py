from pathlib import Path
import os
import tempfile

from alembic.config import Config as AlembicCfg


root_path = Path(".")


class Config:
    def __init__(self):
        self.DATABASE_URI = f"sqlite:///{root_path}/app.db"
        self.ALEMBIC_INI = f"{root_path}/alembic.ini"
        self.ALEMBIC_CFG = self.setup_alembic_config()

    def setup_alembic_config(self):
        alembic_cfg = AlembicCfg(self.ALEMBIC_INI)
        alembic_cfg.set_main_option("sqlalchemy.url", self.DATABASE_URI)
        return alembic_cfg


class TestConfig(Config):
    def __init__(self):
        temp = tempfile.NamedTemporaryFile(suffix=".db")
        self.DATABASE_URI = f"sqlite:///{temp.name}"
        self.ALEMBIC_INI = f"{root_path}/alembic.ini"
        self.ALEMBIC_CFG = self.setup_alembic_config()


class ConfSingleton:
    __config = None

    def get_configuration(self):
        if self.__config:
            return self.__config
        else:
            if os.getenv("TESTING") == "True":
                self.__config = TestConfig()
                return self.__config
            else:
                self.__config = Config()
                return self.__config


def get_conf():
    return ConfSingleton().get_configuration()
