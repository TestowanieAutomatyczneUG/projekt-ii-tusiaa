from src.baza_danych import Baza_Danych
from src.storage.storage_base import Storage_Base
from src.zamowienie import Zamowienie

class Order_Storage:

    def znajdz_zamowienie(self, id):
        if type(id) is not int:
            raise ValueError("id nie jest liczba")
        for zamowienie in Storage_Base.zamowienia:
            if zamowienie.id == id:
                return zamowienie
        return None

    def dodaj_zamowienie(self, zamowienie: Zamowienie):
        if type(zamowienie) is not Zamowienie:
            raise ValueError("zamowienie nie jest obiektem klasy Zamowienie")
        if self.znajdz_zamowienie(zamowienie.id):
            raise ValueError("Zamowienie juz istnieje")
        Storage_Base.zamowienia.append(zamowienie)
        Baza_Danych().dodaj_zamowienie(zamowienie.id, zamowienie.klient_id)

    def usun_zamowienie(self, id):
        if type(id) is not int:
            raise ValueError("id nie jest liczba")
        if not self.znajdz_zamowienie(id):
            raise ValueError("Nie ma takiego zamowienia")
        Storage_Base.zamowienia.remove(self.znajdz_zamowienie(id))
        Baza_Danych().usun_zamowienie(id)

    def dane_zamowienia(self):
        wynik = []
        for zamowienie in Storage_Base.zamowienia:
            wynik.append((zamowienie.id, zamowienie.klient_id))
        return wynik

