import yaml

from root.settings import BASE_DIR
from firma.ClientFileStrategy import ClientFileStrategy


class ClientRepYaml(ClientFileStrategy):

    @classmethod
    def get_data_from_file_specific(cls):
        path_to_file = BASE_DIR / 'db_yaml.yaml'
        with open(path_to_file) as file:
            data = yaml.safe_load(file)
        return data if data else []

    @classmethod
    def write_data_to_file(cls, data):
        path_to_file = BASE_DIR / 'db_yaml.yaml'
        with open(path_to_file, mode='w') as file:
            yaml.dump(data, file)
