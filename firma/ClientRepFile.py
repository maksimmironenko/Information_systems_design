from firma.Client import Client
from common_utils.serializers import ClientSerializer
from root.settings import BASE_DIR
from common_utils.exceptions import FileException


class ClientRepFile:

    def __init__(self, file_strategy):
        self.file_strategy = file_strategy

    def read(self, skip=None, count=None):
        clients = []
        data, _, _ = self.file_strategy.get_data_from_file()
        for entry in data:
            clients.append(Client(**entry))
        return clients[skip:][:count]

    def save(self, clients):
        serializer_class = ClientSerializer
        data, _, emails = self.file_strategy.get_data_from_file()
        for client in clients:
            serialized_data = serializer_class(client).__dict__
            if serialized_data['email'] in emails:
                raise ValueError('Поле email - уникально.')
            data.append(serialized_data)
            emails.append(serialized_data['email'])
        self.file_strategy._write_data_to_file(data)

    def get(self, id):
        data, _, _ = self.file_strategy.get_data_from_file()
        for entry in data:
            if entry['id'] == id:
                return Client(
                    email=entry['email'],
                    phone_number=entry['phone_number'],
                    firstname=entry['firstname'],
                    surname=entry['surname'],
                    fathersname=entry['fathersname'],
                    pasport=entry['pasport'],
                    balance=entry['balance'],
                )
        return None

    def delete(self, id):
        data, ids, _ = self.file_strategy.get_data_from_file()
        data.remove(data[ids.index(id)])
        self.file_strategy.write_data_to_file(data)

    @classmethod
    def sort_by_email(cls):
        pass

    def add(
            self,
            email,
            phone_number,
            firstname,
            surname,
            fathersname,
            pasport,
            balance=None
    ):
        data, ids, emails = self.file_strategy.get_data_from_file()
        if email in emails:
            raise ValueError('Поле email - уникально.')
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
        self.file_strategy.write_data_to_file(data)

    def get_count(self):
        return len(self.read())

    def get_data_from_file(self):
        data = self.file_strategy.get_data_from_file_specific()
        ids = [entry['id'] for entry in data]
        emails = [entry['email'] for entry in data]

        return data, ids, emails
