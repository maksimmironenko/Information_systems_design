import re

import json

from firma.BaseClient import BaseClient


class Client(BaseClient):

    def __init__(
            self,
            email,
            phone_number,
            firstname, 
            surname, 
            fathersname,
            pasport,
            balance=None,
            id=None,
        ):
        super(Client, self).__init__(id=id, email=email, firstname=firstname, surname=surname, fathersname=fathersname)
        self.set_id(id)
        self.set_phone_number(phone_number)
        self.set_pasport(pasport)
        self.set_balance(balance)
    
    def set_phone_number(self, phone_number):
        if not self.__validate_phone_number(phone_number):
            raise ValueError('Неверный номер телефона.')
        self._phone_number = phone_number

    def set_pasport(self, pasport):
        if not self.__validate_pasport(pasport):
            raise ValueError('Неверные паспортные данные.')
        self._pasport = pasport
    
    def set_balance(self, balance):
        if not self.__validate_balance(balance):
            raise ValueError('Неверный баланс.')
        self._balance = balance
    
    def get_phone_number(self):
        return self._phone_number
    
    def get_pasport(self):
        return self._pasport
    
    def get_balance(self):
        return self._balance
    
    @staticmethod
    def __validate_phone_number(phone_number):
        if not isinstance(phone_number, str) or not re.fullmatch(r'((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}', phone_number):
            return False
        return True
    
    @staticmethod
    def __validate_pasport(pasport):
        if not isinstance(pasport, str) or not re.fullmatch(r'\d{4} \d{6}', pasport):
            return False
        return True
    
    @staticmethod
    def __validate_balance(balance):
        if balance is not None:
            if not isinstance(balance, (float, int)) or balance < 0:
                return False
        return True
    
    @classmethod
    def from_json(cls, json_str):
        fields = json.loads(json_str)
        return cls(
            id=fields['id'],
            email=fields['email'],
            phone_number=fields['phone_number'],
            firstname=fields['firstname'],
            surname=fields['surname'],
            fathersname=fields['fathersname'],
            pasport=fields['pasport'],
            balance=fields['balance'],
        )
    
    @property
    def full_information(self):
        return (
            self.get_id(),
            self.get_surname(), 
            self.get_firstname(), 
            self.get_fathersname(),
            self.get_email(),
            self.get_pasport(), 
            self.get_phone_number(),
            self.get_balance(),
        )
    
    @property
    def short_information(self):
        return (
            self.get_surname(), 
            self.get_firstname(), 
            self.get_fathersname(),
            self.get_email(),
        )
