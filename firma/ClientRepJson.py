import json

from root.settings import BASE_DIR
from firma.ClientFileStrategy import ClientFileStrategy


class ClientRepJson(ClientFileStrategy):

    @staticmethod
    def get_data_from_file_specific():
        path_to_file = BASE_DIR / 'db_json.json'
        with open(path_to_file) as file:
            try:
                data = json.loads(file.read())
            except json.decoder.JSONDecodeError:
                data = []
        return data

    @staticmethod
    def write_data_to_file(data):
        path_to_file = BASE_DIR / 'db_json.json'
        with open(path_to_file, mode='w') as file:
            file.write(json.dumps(data))
