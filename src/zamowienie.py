from src.baza_danych import Baza_Danych
from src.przedmiot import Przedmiot

class Zamowienie:
    def __init__(self, id: int, klient_id: int):
        if type(id) is not int:
            raise ValueError("id nie jest liczba")
        if type(klient_id) is not int:
            raise ValueError("klient_id nie jest liczba")
        self.id = id
        self.klient_id = klient_id
        self.przedmioty = []