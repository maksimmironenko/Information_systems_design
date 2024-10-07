from builtins import NotImplementedError

from firma.ClientRepFile import ClientRepFile


class ClientFileStrategy:

    def get_data_from_file_specific(self):
        raise NotImplementedError('This method shod be implemented.')

    def write_data_to_file(self, data):
        raise NotImplementedError('This method shod be implemented.')
