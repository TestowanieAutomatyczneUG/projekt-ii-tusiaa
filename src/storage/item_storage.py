from src.baza_danych import Baza_Danych
from src.storage.storage_base import Storage_Base
from src.przedmiot import Przedmiot

class Item_Storage:

    def znajdz_przedmiot(self, id):
        if type(id) is not int:
            raise ValueError("id nie jest liczba")
        for przedmiot in Storage_Base.przedmioty:
            if przedmiot.id == id:
                return przedmiot
        return None

    def dodaj_przedmiot(self, przedmiot: Przedmiot):
        if type(przedmiot) is not Przedmiot:
            raise ValueError("przedmiot nie jest obiektem klasy Przedmiot")
        if self.znajdz_przedmiot(przedmiot.id):
            raise ValueError("Przedmiot juz istnieje")
        Storage_Base.przedmioty.append(przedmiot)
        Baza_Danych().dodaj_przedmiot(przedmiot.id, przedmiot.nazwa, przedmiot.wartosc)

    def usun_przedmiot(self, id):
        if type(id) is not int:
            raise ValueError("id nie jest liczba")
        if not self.znajdz_przedmiot(id):
            raise ValueError("Nie ma takiego przedmiotu")
        Storage_Base.przedmioty.remove(self.znajdz_przedmiot(id))
        Baza_Danych().usun_przedmiot(id)

    def dane_przedmioty(self):
        wynik = []
        for przedmiot in Storage_Base.przedmioty:
            wynik.append((przedmiot.id, przedmiot.nazwa, przedmiot.wartosc))
        return wynik


