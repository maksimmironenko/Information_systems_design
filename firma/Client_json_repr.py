from firma.Client import Client

class Client_json_repr(Client):

    def __init__(self, *args, **kwargs):
        super(Client_json_repr, self).__init__(*args, **kwargs)

    @classmethod
    def from_json_file(cls, path_to_file):
        clients = []
        with open(path_to_file) as file:
            data = file.read()
            for entry in json.loads(data):
                clients.append(
                    super().from_json(f'{entry}')
                )
        return clients

    @classmethod
    def to_json_file(cls, path_to_file, clients, do_not_truncate_file=False):
        mode = 'w'
        if do_not_truncate_file:
            mode = 'a'

        with open(path_to_file, mode=mode) as file:
            file.write('[')
            for client in clients:
                json_entry = json.dumps(client)
                file.write(json_entry)
                file.write(',')
            file.write(']')
