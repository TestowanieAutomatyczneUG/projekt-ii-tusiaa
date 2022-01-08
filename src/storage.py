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

    def dodaj_klienta(self, klient: Klient):
        if type(klient) is not Klient:
            raise ValueError("klient nie jest obiektem klasy Klient")
        if Baza_Danych().znajdz_klienta(klient.id):
            raise ValueError("Klient juz istnieje")
        self.klienci.append(klient)
        Baza_Danych().dodaj_klienta(klient.id, klient.imie, klient.nazwisko, klient.email)