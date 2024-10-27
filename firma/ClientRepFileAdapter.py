from firma.ClientRepFile import ClientRepFile


class ClientRepFileAdapter:

    def __init__(self, client_rep_file: ClientRepFile):
        client_rep_file.read_data_from_file()
        self._client_rep_file = client_rep_file

    def get_short_list(self, skip=None, count=None):
        return self._client_rep_file.get_short_list(skip, count)

    def get(self, id):
        return self._client_rep_file.get(id)

    def delete(self, id):
        self._client_rep_file.delete(id)
        self._client_rep_file.write_data_to_file()

    def change(
            self,
            id,
            email=None,
            phone_number=None,
            firstname=None,
            surname=None,
            fathersname=None,
            pasport=None,
            balance=None,
    ):
        self._client_rep_file.change(
            id,
            email,
            phone_number,
            firstname,
            surname,
            fathersname,
            pasport,
            balance,
        )
        self._client_rep_file.write_data_to_file()

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
        self._client_rep_file.add(
            email,
            phone_number,
            firstname,
            surname,
            fathersname,
            pasport,
            balance,
        )
        self._client_rep_file.write_data_to_file()

    def get_count(self):
        return self._client_rep_file.get_count()
