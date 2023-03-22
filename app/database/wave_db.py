from peewee import PostgresqlDatabase

from ..config import settings


class WaveDB:
    def __init__(self):
        self.__db = None

    @property
    def db(self):
        if self.__db is None:
            host = settings.DB_HOST
            user = settings.DB_USER
            password = settings.DB_PASS
            database = settings.DB_NAME

            self.__db = PostgresqlDatabase(database, host=host, user=user, password=password)

        return self.__db


wave_db = WaveDB()
