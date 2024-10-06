import psycopg2
from psycopg2 import OperationalError


class DBConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DBConnection, cls).__new__(cls)
            cls._instance._connection = cls._create_connection(
                db_name='pg_database',
                db_host='127.0.0.1',
                db_port='5432',
                db_user='postgres',
                db_password='postgres',
            )
        return cls._instance

    def get_connection(self):
        return self._connection

    @staticmethod
    def _create_connection(db_name, db_user, db_password, db_host, db_port):
        connection = None
        try:
            print('Start connection')
            connection = psycopg2.connect(
                database=db_name,
                user=db_user,
                password=db_password,
                host=db_host,
                port=db_port,
            )
            print("Connection to PostgreSQL DB successful")
        except OperationalError as e:
            print(f"The error '{e}' occurred")
        return connection