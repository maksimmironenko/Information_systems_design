class Client:
    """Класс клиента"""

    def __init__(
            self,
            email: str,
            phone_number: str,
            firstname: str, 
            surname: str, 
            fathersname: str|None,
            pasport: str,
            balance: float|None=None
        ):
        self.set_email(email)
        self.set_phone_number(phone_number)
        self.set_firstname(firstname)
        self.set_surname(surname)
        self.set_fathersname(fathersname)
        self.set_pasport(pasport)
        self.set_balance(balance)

    def set_email(self, email: str):
        self._email = email
    
    def set_phone_number(self, phone_number: str):
        self._phone_number = phone_number

    def set_firstname(self, firstname: str):
        self._firstname = firstname
    
    def set_surname(self, surname: str):
        self._surname = surname

    def set_fathersname(self, fathersname: str|None):
        self._fathersname = fathersname

    def set_pasport(self, pasport: str):
        self._pasport = pasport
    
    def set_balance(self, balance: float|None):
        self._balance = balance

    def get_email(self):
        return self._email
    
    def get_phone_number(self):
        return self._phone_number
    
    def get_firstname(self):
        return self._firstname
    
    def get_surname(self):
        return self._surname
    
    def get_fathersname(self):
        return self._fathersname
    
    def get_pasport(self):
        return self._pasport
    
    def get_balance(self):
        return self._balance
    
    def __str__(self)->str:
        return f'{self._surname} {self._firstname}'
