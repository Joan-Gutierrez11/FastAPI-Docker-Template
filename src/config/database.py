from pydantic import MariaDBDsn
from pydantic_settings import BaseSettings

class DBSettings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DB_PASS: str
    DB_USER: str

    @property
    def url(self):
        return MariaDBDsn.build(
            scheme='mariadb+pymysql',
            host=self.DB_HOST,
            password=self.DB_PASS,
            username=self.DB_USER,
            port=self.DB_PORT,
            path=self.DB_NAME
        ).encoded_string()
    
db = DBSettings()
