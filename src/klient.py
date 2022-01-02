from src.baza_danych import Baza_Danych

class Klient:
    def __init__(self, id, imie, nazwisko, email):
        self.id = id
        self.imie = imie
        self.nazwisko = nazwisko
        self.email = email
        self.zamowienia = []