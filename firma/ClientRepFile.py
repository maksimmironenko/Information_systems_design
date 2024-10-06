from firma.Client import Client
from common_utils.serializers import ClientSerializer
from root.settings import BASE_DIR
from common_utils.exceptions import FileException


class ClientRepFile:

    @classmethod
    def read(cls, skip=None, count=None):
        clients = []
        data, _ = cls._get_data_from_file()
        for entry in data:
            clients.append(Client(**entry))
        return clients[skip:][:count]

    @classmethod
    def save(cls, clients):
        serializer_class = ClientSerializer
        data, ids = cls._get_data_from_file()
        for client in clients:
            serialized_data = serializer_class(client).__dict__
            if serialized_data['id'] in ids:
                data[ids.index(serialized_data['id'])] = serialized_data
            else:
                data.append(serialized_data)
        cls._write_data_to_file(data)

    @classmethod
    def get(cls, id):
        data, _ = cls._get_data_from_file()
        for entry in data:
            if entry['id'] == id:
                return Client(**entry)
        return None

    @classmethod
    def delete(cls, id):
        data, ids = cls._get_data_from_file()
        data.remove(data[ids.index(id)])
        cls._write_data_to_file(data)

    @classmethod
    def sort_by_email(cls):
        pass

    @classmethod
    def add(
            cls,
            id,
            email,
            phone_number,
            firstname,
            surname,
            fathersname,
            pasport,
            balance=None
    ):
        data, ids = cls._get_data_from_file()
        ids.sort()

        id = 0
        if ids:
            id = ids[-1]
        id += 1

        data.append(
            {
                'id': id,
                'email': email,
                'phone_number': phone_number,
                'firstname': firstname,
                'surname': surname,
                'fathersname': fathersname,
                'pasport': pasport,
                'balance': balance,
            }
        )
        cls._write_data_to_file(data)

    @classmethod
    def get_count(cls):
        return len(cls.read())

    @classmethod
    def _get_data_from_file(cls):
        try:
            data = cls._get_data_from_file_specific()
            if data is None:
                data = []
            ids = [entry['id'] for entry in data] if data else []
        except FileException:
            data = []
            ids = []

        return data, ids

    @classmethod
    def _write_data_to_file(cls, data):
        raise NotImplementedError("This method should be implemented in a subclass")

    @classmethod
    def _get_data_from_file_specific(cls):
        raise NotImplementedError("This method should be implemented in a subclass")
