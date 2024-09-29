class ClientSerializer:
    def __init__(self, client):
        self.id = client.get_id()
        self.firstname = client.get_firstname()
        self.surname = client.get_surname()
        self.fathersname = client.get_fathersname()
        self.phone_number = client.get_phone_number()
        self.pasport = client.get_pasport()
        self.balance = client.get_balance()
        self.email = client.get_email()