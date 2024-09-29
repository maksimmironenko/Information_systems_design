import json

from common_utils.serializers import ClientSerializer
from root.settings import BASE_DIR
from firma.Client import Client


class Client_json_repr(Client):

    def __init__(self, *args, **kwargs):
        super(Client_json_repr, self).__init__(*args, **kwargs)

    @classmethod
    def read(cls):
        path_to_file = BASE_DIR / 'db_json.json'
        clients = []
        with open(path_to_file) as file:
            data = file.read()
            for entry in json.loads(data):
                clients.append(Client(**entry))
        return clients

    @classmethod
    def save(cls, clients):
        serializer_class = ClientSerializer
        path_to_file = BASE_DIR / 'db_json.json'
        ids = []
        with open(path_to_file) as file:
            try:
                data = json.loads(file.read())
                ids = [entry['id'] for entry in data]
            except json.decoder.JSONDecodeError:
                data = []
        with open(path_to_file, mode='w') as file:
            for client in clients:
                serialized_data = serializer_class(client).__dict__
                if serialized_data['id'] in ids:
                    data[ids.index(serialized_data['id'])] = serialized_data
                else:
                    data.append(serialized_data)
            file.write(json.dumps(data))

    @classmethod
    def get(cls, id):
        path_to_file = BASE_DIR / 'db_json.json'
        with open(path_to_file, mode='r') as file:
                data = json.loads(file.read())
        for entry in data:
            if entry['id'] == id:
                return Client(**entry)
        return None
