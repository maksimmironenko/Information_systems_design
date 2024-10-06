import json

from root.settings import BASE_DIR
from firma.ClientRepFile import ClientRepFile


class ClientRepJson(ClientRepFile):

    @classmethod
    def _get_data_from_file_specific(cls):
        path_to_file = BASE_DIR / 'db_json.json'
        with open(path_to_file) as file:
            data = json.loads(file.read())
        return data

    @classmethod
    def _write_data_to_file(cls, data):
        path_to_file = BASE_DIR / 'db_json.json'
        with open(path_to_file, mode='w') as file:
            file.write(json.dumps(data))
