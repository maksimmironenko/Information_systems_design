import yaml

from root.settings import BASE_DIR
from firma.ClientRepFile import ClientRepFile


class ClientRepYaml(ClientRepFile):

    @classmethod
    def _get_data_from_file(cls):
        path_to_file = BASE_DIR / 'db_yaml.yaml'
        with open(path_to_file) as file:
            try:
                data = yaml.safe_load(file)
                if data is None:
                    data = []
                ids = [entry['id'] for entry in data] if data else []
            except yaml.YAMLError:
                data = []
                ids = []

        return data, ids

    @classmethod
    def _write_data_to_file(cls, data):
        path_to_file = BASE_DIR / 'db_yaml.yaml'
        with open(path_to_file, mode='w') as file:
            yaml.dump(data, file)
