from builtins import NotImplementedError

from firma.ClientRepFile import ClientRepFile


class ClientFileStrategy:

    @staticmethod
    def read_data_from_file():
        raise NotImplementedError('This method shod be implemented.')

    @staticmethod
    def write_data_to_file(data):
        raise NotImplementedError('This method shod be implemented.')
