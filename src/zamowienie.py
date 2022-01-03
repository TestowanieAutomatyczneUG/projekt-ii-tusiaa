from src.baza_danych import Baza_Danych
from src.przedmiot import Przedmiot

class Zamowienie:
    def __init__(self, id, klient_id):
        self.id = id
        self.klient_id = klient_id
        self.przedmioty = []