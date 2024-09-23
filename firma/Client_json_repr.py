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
    def to_json_file(cls, path_to_file, clients, extend_file=False):
        mode = 'w'
        if extend_file:
            mode = 'ra'
        data = []
        with open(path_to_file, mode=mode) as file:
            if extend_file:
                data = json.loads(file.read())
            for client in clients:
                data.append(client.__dict__)
            file.write(json.dumps(data))
