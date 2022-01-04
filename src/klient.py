from src.baza_danych import Baza_Danych
from src.zamowienie import Zamowienie

class Klient:
    def __init__(self, id, imie, nazwisko, email):
        if type(id) is not int:
            raise ValueError("id nie jest liczba")
        if type(imie) is not str or not imie:
            raise ValueError("imie nie jest stringiem")
        if type(nazwisko) is not str or not nazwisko:
            raise ValueError("nazwisko nie jest stringiem")
        if type(email) is not str or not email:
            raise ValueError("email nie jest stringiem")
        self.id = id
        self.imie = imie
        self.nazwisko = nazwisko
        self.email = email
        self.zamowienia = []