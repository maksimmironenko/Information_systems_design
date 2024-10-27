from common_utils.db_connection import DBConnection


class ClientRepDB:

    def __init__(self):
        self._connection = DBConnection().get_connection()
        with self._connection.cursor() as cur:
            cur.execute(
                "CREATE TABLE IF NOT EXISTS client (id serial primary key, email varchar unique, phone_number varchar, firstname varchar, surname varchar, fathersname varchar, pasport varchar, balance double precision);")
            self._connection.commit()

    def get_short_list(self, skip=None, count=None):
        with self._connection.cursor() as cur:
            cur.execute(f"""
            SELECT * FROM
            client
            OFFSET {skip if skip else 'null'}
            LIMIT {count if count else 'null'};
            """)
            return [entry for entry in cur.fetchall()]

    def get(self, id):
        if not isinstance(id, int):
            raise ValueError('id должен быть int.')
        with self._connection.cursor() as cur:
            cur.execute(f"SELECT * FROM client c WHERE c.id = {id};")
            return cur.fetchone()

    def delete(self, id):
        with self._connection.cursor() as cur:
            cur.execute(f"""
                   DELETE FROM client c
                   WHERE c.id = {id}; 
               """)
            self._connection.commit()

    def change(
        self,
        id,
        email,
        phone_number,
        firstname,
        surname,
        fathersname,
        pasport,
        balance,
    ):
        with self._connection.cursor() as cur:
            cur.execute(
                f"""
                    UPDATE client c
                    SET 
                        firstname='{firstname}', 
                        surname='{surname}', 
                        phone_number='{phone_number}', 
                        pasport='{pasport}', 
                        balance={balance if balance is not None else 'null'}, 
                        email='{email}',
                        fathersname={"'" if fathersname else ''}{fathersname if fathersname else 'null'}{"'" if fathersname else ''}
                    WHERE c.id = {id};
                """
            )

    def add(
        self,
        email,
        phone_number,
        firstname,
        surname,
        fathersname,
        pasport,
        balance=None,
    ):
        with self._connection.cursor() as cur:
            cur.execute(f"""
            INSERT INTO client 
            (firstname, surname, phone_number, pasport, balance, email, fathersname) 
            VALUES(
                '{firstname}', 
                '{surname}',
                '{phone_number}',
                '{pasport}',
                 {balance if balance is not None else 'null'},
                '{email}',
                {"'" if fathersname else ''}{fathersname if fathersname else 'null'}{"'" if fathersname else ''}
            )
            """)
            self._connection.commit()

    def get_count(self):
        with self._connection.cursor() as cur:
            cur.execute("SELECT COUNT(*) FROM client;")
            return cur.fetchone()[0]
