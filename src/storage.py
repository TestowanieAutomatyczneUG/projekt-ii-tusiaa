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

    def znajdz_klienta(self, id):
        if type(id) is not int:
            raise ValueError("id nie jest liczba")
        for klient in self.klienci:
            if klient.id == id:
                return klient
        return None

    def dodaj_klienta(self, klient: Klient):
        if type(klient) is not Klient:
            raise ValueError("klient nie jest obiektem klasy Klient")
        if Baza_Danych().znajdz_klienta(klient.id):
            raise ValueError("Klient juz istnieje")
        self.klienci.append(klient)
        Baza_Danych().dodaj_klienta(klient.id, klient.imie, klient.nazwisko, klient.email)

    def usun_klienta(self, id):
        if type(id) is not int:
            raise ValueError("id nie jest liczba")
        if not Baza_Danych().znajdz_klienta(id):
            raise ValueError("Nie ma takiego klienta")
        self.klienci.remove(self.znajdz_klienta(id))
        Baza_Danych().usun_klienta(id)

    def dane_klienci(self):
        wynik = []
        for klient in self.klienci:
            wynik.append((klient.id, klient.imie, klient.nazwisko, klient.email))
        return wynik

    def dane_zamowienia(self):
        wynik = []
        for zamowienie in self.zamowienia:
            wynik.append((zamowienie.id, zamowienie.klient_id))
        return wynik

    def dane_przedmioty(self):
        wynik = []
        for przedmiot in self.przedmioty:
            wynik.append((przedmiot.id, przedmiot.nazwa, przedmiot.wartosc))
        return wynik
