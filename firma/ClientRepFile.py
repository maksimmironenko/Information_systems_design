from firma.Client import Client
from common_utils.serializers import ClientSerializer


class ClientRepFile:

    def __init__(self, file_strategy):
        self._data = []
        self.file_strategy = file_strategy

    def get_short_list(self, skip=None, count=None):
        return self._data[skip:][:count]

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
        for entry in self._data:
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
        ids = self.__ids()
        self._data.remove(self._data[ids.index(id)])
        self.file_strategy.write_data_to_file(self._data)

    def sort_by_email(self):
        self._data.sort(key=lambda entry: entry['email'])

    def change(
        self,
        id,
        email,
        phone_number,
        firstname, 
        surname, 
        fathersname,
        pasport,
        balance=None,
    ):
        ids, emails = self.__ids(), self.__emails()
        index = ids.index(id)
        data = {
            'id': id,
            'email': email,
            'phone_number': phone_number,
            'firstname': firstname, 
            'surname': surname, 
            'fathersname': fathersname,
            'pasport': pasport,
            'balance': balance,
        }
        if email != self._data[ids.index(id)]['email'] and email in emails:
            raise ValueError('Поле email - уникально.')
        self._data[index] = data
        self.file_strategy.write_data_to_file(self._data)

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
        ids, emails = self.__ids(), self.__email()
        if email in emails:
            raise ValueError('Поле email - уникально.')
        ids.sort()

        id = 0
        if ids:
            id = ids[-1]
        id += 1

        self._data.append(
            {
                'id': id,
                'email': email,
                'phone_number': phone_number,
                'firstname': firstname, 
                'surname': surname, 
                'fathersname': fathersname,
                'pasport'; pasport,
                'balance': balance,
            }
        )
        self.file_strategy.write_data_to_file(self._data)

    def get_count(self):
        return len(self._data)

    def get_data_from_file(self):
        data = self.file_strategy.get_data_from_file_specific()
        self._data = data

    def __ids(self):
        return [entry['id'] for entry in self._data]

    def __emails(self):
        return [entry['email'] for entry in self._data]
