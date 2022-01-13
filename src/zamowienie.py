from src.baza_danych import Baza_Danych
from src.storage.item_storage import *
from src.storage.client_storage import *

class Zamowienie:
    def __init__(self, id: int, klient_id: int):
        if type(id) is not int:
            raise ValueError("id nie jest liczba")
        if type(klient_id) is not int:
            raise ValueError("klient_id nie jest liczba")
        if not Baza_Danych.znajdz_klienta(klient_id):
            raise ValueError("Nie ma takiego klienta")
        self.id = id
        self.klient_id = klient_id
        self.przedmioty = []

    def dodaj_przedmiot(self, przedmiot_id: int):
        if type(przedmiot_id) is not int:
            raise ValueError("przedmiot_id nie jest liczba")
        if not Item_Storage.znajdz_przedmiot(przedmiot_id):
            raise ValueError("Nie ma takiego przedmiotu")
        self.przedmioty.append(przedmiot_id)
        Baza_Danych().dodaj_przedmiot_do_zamowienia(self.id, przedmiot_id)

    def usun_przedmiot(self, przedmiot_id: int):
        if type(przedmiot_id) is not int:
            raise ValueError("przedmiot_id nie jest liczba")
        if przedmiot_id not in self.przedmioty:
            raise ValueError("Nie ma takiego przedmiotu")
        self.przedmioty.remove(przedmiot_id)
        Baza_Danych().usun_przedmiot_z_zamowienia(self.id, przedmiot_id)

    def czy_jest_przedmiot(self, przedmiot_id: int):
        if type(przedmiot_id) is not int:
            raise ValueError("przedmiot_id nie jest liczba")
        if przedmiot_id not in self.przedmioty:
            return False
        return True

    def dane_klient(self):
        return Client_Storage.znajdz_klienta(self.klient_id)

    def dane_przedmioty(self):
        wynik = []
        for przedmiot_id in self.przedmioty:
            wynik.append(Item_Storage.znajdz_przedmiot(przedmiot_id))
        return wynik
