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

    def dodaj_zamowienie(self, id):
        if type(id) is not int:
            raise ValueError("id nie jest liczba")
        self.zamowienia.append(id)
        Baza_Danych().dodaj_zamowienie(id, self.id)

    def usun_zamowienie(self, id):
        if type(id) is not int:
            raise ValueError("id nie jest liczba")
        if id not in self.zamowienia:
            raise ValueError("Nie ma takiego zamowienia")
        self.zamowienia.remove(id)
        Baza_Danych().usun_zamowienie(id)

    def zmien_imie(self, imie):
        if type(imie) is not str or not imie:
            raise ValueError("imie nie jest stringiem")
        self.imie = imie
        Baza_Danych().edytuj_klienta(self.id, self.imie, self.nazwisko, self.email)

    def zmien_nazwisko(self, nazwisko):
        if type(nazwisko) is not str or not nazwisko:
            raise ValueError("nazwisko nie jest stringiem")
        self.nazwisko = nazwisko
        Baza_Danych().edytuj_klienta(self.id, self.imie, self.nazwisko, self.email)

    def zmien_email(self, email):
        if type(email) is not str or not email:
            raise ValueError("email nie jest stringiem")
        self.email = email
        Baza_Danych().edytuj_klienta(self.id, self.imie, self.nazwisko, self.email)

