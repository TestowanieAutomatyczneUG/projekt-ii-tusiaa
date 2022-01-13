from src.baza_danych import Baza_Danych
from src.storage.storage_base import Storage_Base
from src.klient import Klient

class Client_Storage:

    def znajdz_klienta(self, id):
        if type(id) is not int:
            raise ValueError("id nie jest liczba")
        for klient in Storage_Base.klienci:
            if klient.id == id:
                return klient
        return None

    def dodaj_klienta(self, klient: Klient):
        if type(klient) is not Klient:
            raise ValueError("klient nie jest obiektem klasy Klient")
        if self.znajdz_klienta(klient.id):
            raise ValueError("Klient juz istnieje")
        Storage_Base.klienci.append(klient)
        Baza_Danych.dodaj_klienta(klient.id, klient.imie, klient.nazwisko, klient.email)    

    def usun_klienta(self, id):
        if type(id) is not int:
            raise ValueError("id nie jest liczba")
        if not self.znajdz_klienta(id):
            raise ValueError("Nie ma takiego klienta")
        Storage_Base.klienci.remove(self.znajdz_klienta(id))
        Baza_Danych.usun_klienta(id)

    def dane_klienci(self):
        wynik = []
        for klient in Storage_Base.klienci:
            wynik.append((klient.id, klient.imie, klient.nazwisko, klient.email))
        return wynik



