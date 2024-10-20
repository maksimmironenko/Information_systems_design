from firma.Client import Client
from common_utils.serializers import ClientSerializer


class ClientRepFile:

    def __init__(self, file_strategy):
        self.file_strategy = file_strategy

    def read(self, skip=None, count=None):
        clients = []
        data, _, _ = self.get_data_from_file()
        for entry in data:
            clients.append(
                Client(
                    email=entry['email'],
                    phone_number=entry['phone_number'],
                    firstname=entry['firstname'],
                    surname=entry['surname'],
                    fathersname=entry['fathersname'],
                    pasport=entry['pasport'],
                    balance=entry['balance'],
                )
            )
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
        self.file_strategy.write_data_to_file(data)

    def get(self, id):
        data, _, _ = self.get_data_from_file()
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
        data, ids, _ = self.get_data_from_file()
        data.remove(data[ids.index(id)])
        self.file_strategy.write_data_to_file(data)

    @classmethod
    def sort_by_email(cls):
        pass

    def add(
            self,
            client,
    ):
        data, ids, emails = self.get_data_from_file()
        if client.get_email() in emails:
            raise ValueError('Поле email - уникально.')
        ids.sort()

        id = 0
        if ids:
            id = ids[-1]
        id += 1

        data.append(
            {
                'id': id,
                **ClientSerializer(client).__dict__,
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
