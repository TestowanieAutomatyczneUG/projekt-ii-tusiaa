from src.klient import Klient
from src.zamowienie import Zamowienie
from src.przedmiot import Przedmiot
from src.baza_danych import Baza_Danych

class Storage:
    def __init__(self):
        self.klienci = []
        self.przedmioty = []
        self.zamowienia = []
        self.przedmioty_w_zamowieniach = []
