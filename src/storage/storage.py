from src.baza_danych import Baza_Danych
from src.storage.storage_base import Storage_Base
from src.storage.item_storage import *
from src.storage.order_storage import *
from src.storage.client_storage import *

class Storage:

    def importuj_z_bazy(self):
        klienci = Baza_Danych().czytaj_klientow()
        przedmioty = Baza_Danych().czytaj_przedmioty()
        zamowienia = Baza_Danych().czytaj_zamowienia()
        relacje = Baza_Danych().czytaj_przedmioty_z_zamowien()

        for przedmiot in przedmioty:
            Storage_Base.przedmioty.append(Przedmiot(przedmiot[0], przedmiot[1], przedmiot[2]))

        for klient in klienci:
            Storage_Base.klienci.append(Klient(klient[0], klient[1], klient[2], klient[3]))

        for zamowienie in zamowienia:
            Storage_Base.zamowienia.append(Zamowienie(zamowienie[0], zamowienie[1]))

        for relacja in relacje:
            Storage_Base.przedmioty_w_zamowieniach.append(relacja)

        for klient in klienci:
            for zamowienie in zamowienia:
                if zamowienie[1] == klient[0]:
                    Client_Storage.znajdz_klienta(klient[0]).dodaj_zamowienie(zamowienie[0])
                    for przedmiot in relacje:
                        if przedmiot[1] == zamowienie[0]:
                            Order_Storage.znajdz_zamowienie(zamowienie[0]).dodaj_przedmiot(przedmiot[0])
