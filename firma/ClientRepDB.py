from common_utils.db_connection import DBConnection
from common_utils.serializers import ClientSerializer

class ClientRepDB:

    def __init__(self):
        self._connection = DBConnection().get_connection()
        with self._connection.cursor() as cur:
            cur.execute(
                "CREATE TABLE IF NOT EXISTS client (id serial primary key, email varchar unique, phone_number varchar, firstname varchar, surname varchar, fathersname varchar, pasport varchar, balance double precision);")
            self._connection.commit()

    def read(self, skip=None, count=None):
        with self._connection.cursor() as cur:
            cur.execute(f"""
            SELECT * FROM
            client
            OFFSET {skip if skip else 'null'}
            LIMIT {count if count else 'null'};
            """)
            return [ClientSerializer.from_pg_sql(entry) for entry in cur.fetchall()]

    def get_count(self):
        return len(self.read())

    def get(self, id):
        if not isinstance(id, int):
            raise ValueError('id должен быть int.')
        with self._connection.cursor() as cur:
            cur.execute(f"SELECT * FROM client c WHERE c.id = {id};")
            obj = ClientSerializer.from_pg_sql(cur.fetchone())
        return obj

    def add(self, client):
        with self._connection.cursor() as cur:
            cur.execute(f"""
            INSERT INTO client 
            (firstname, surname, phone_number, pasport, balance, email, fathersname) 
            VALUES(
                '{client.get_firstname()}', 
                '{client.get_surname()}',
                '{client.get_phone_number()}',
                '{client.get_pasport()}',
                 {client.get_balance() if client.get_balance() is not None else 'null'},
                '{client.get_email()}',
                {"'" if client.get_fathersname() else ''}{client.get_fathersname() if client.get_fathersname() else 'null'}{"'" if client.get_fathersname() else ''}
            )
            """)
            self._connection.commit()

    def delete(self, id):
        with self._connection.cursor() as cur:
            cur.execute(f"""
                DELETE FROM client c
                WHERE c.id = {id}; 
            """)
            self._connection.commit()

    def change(self, id, client):
        with self._connection.cursor() as cur:
            cur.execute(
                f"""
                    UPDATE client c
                    SET 
                        firstname='{client.get_firstname()}', 
                        surname='{client.get_surname()}', 
                        phone_number='{client.get_phone_number()}', 
                        pasport='{client.get_pasport()}', 
                        balance={client.get_balance() if client.get_balance() is not None else 'null'}, 
                        email='{client.get_email()}', 
                        fathersname={"'" if client.get_fathersname() else ''}{client.get_fathersname() if client.get_fathersname() else 'null'}{"'" if client.get_fathersname() else ''}
                    WHERE c.id = {id};
                """
            )
