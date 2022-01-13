import unittest
from assertpy import *
from unittest.mock import *
from src.storage.client_storage import *
from src.storage.order_storage import *
from src.storage.item_storage import *
from src.storage.storage_base import *

class TestsStorage(unittest.TestCase):

    @patch.object(Baza_Danych, 'znajdz_klienta', return_value=(11, "Jan", "Kowalski", "mail"))
    @patch.object(Baza_Danych, 'czytaj_klientow', return_value=[(11, "Jan", "Kowalski", "mail")])
    @patch.object(Baza_Danych, 'czytaj_zamowienia', return_value=[(1, 11)])
    @patch.object(Baza_Danych, 'czytaj_przedmioty_z_zamowien', return_value=[(1, 111)])
    @patch.object(Baza_Danych, 'czytaj_przedmioty', return_value=[(111, "Nazwa", 100.0)])
    def setUp(self, mock_czytaj_przedmioty, mock_czytaj_przedmioty_z_zamowien, mock_czytaj_zamowienia, mock_czytaj_klientow, mock_znajdz_klienta):
        Storage_Base.klienci = [Klient(mock_czytaj_klientow()[0][0], mock_czytaj_klientow()[0][1], mock_czytaj_klientow()[0][2], mock_czytaj_klientow()[0][3])]
        Storage_Base.zamowienia = [Zamowienie(mock_czytaj_zamowienia()[0][0], mock_czytaj_zamowienia()[0][1])]
        Storage_Base.przedmioty = [Przedmiot(mock_czytaj_przedmioty()[0][0], mock_czytaj_przedmioty()[0][1], mock_czytaj_przedmioty()[0][2])]
        Storage_Base.przedmioty_w_zamowieniach = [(mock_czytaj_przedmioty_z_zamowien()[0][0], mock_czytaj_przedmioty_z_zamowien()[0][1])]
        self.client_storage = Client_Storage()
        self.order_storage = Order_Storage()
        self.item_storage = Item_Storage()

    def test_storage_init(self):
        assert_that(Storage_Base).is_not_none()

    @patch.object(Baza_Danych, 'dodaj_klienta')
    def test_storage_add_client(self, mock_dodaj_klienta):
        klient = Klient(12, "Jan", "Kowalski", "mail")
        self.client_storage.dodaj_klienta(klient)
        assert_that(Storage_Base.klienci).contains(klient)

    @patch.object(Baza_Danych, 'dodaj_klienta')
    def test_storage_add_client_database_check(self, mock_dodaj_klienta):
        klient = Klient(12, "Jan", "Kowalski", "mail")
        self.client_storage.dodaj_klienta(klient)
        mock_dodaj_klienta.assert_called_once_with(klient.id, klient.imie, klient.nazwisko, klient.email)

    @patch.object(Baza_Danych, 'dodaj_klienta')
    def test_storage_add_client_already_exists(self, mock_dodaj_klienta):
        assert_that(self.client_storage.dodaj_klienta).raises(ValueError).when_called_with(Storage_Base.klienci[0].id)

    @patch.object(Baza_Danych, 'znajdz_klienta', return_value=(11, "Jan", "Kowalski", "mail"))
    @patch.object(Baza_Danych, 'dodaj_zamowienie')
    def test_storage_add_order(self, mock_dodaj_zamowienie, mock_znajdz_klienta):
        zamowienie = Zamowienie(2, 11)
        self.order_storage.dodaj_zamowienie(zamowienie)
        assert_that(Storage_Base.zamowienia).contains(zamowienie)

    @patch.object(Baza_Danych, 'znajdz_klienta', return_value=(11, "Jan", "Kowalski", "mail"))
    @patch.object(Baza_Danych, 'dodaj_zamowienie')
    def test_storage_add_order_database_check(self, mock_dodaj_zamowienie, mock_znajdz_klienta):
        zamowienie = Zamowienie(2, 11)
        self.order_storage.dodaj_zamowienie(zamowienie)
        mock_dodaj_zamowienie.assert_called_once_with(zamowienie.id, zamowienie.klient_id)

    def test_storage_add_order_already_exists(self):
        assert_that(self.order_storage.dodaj_zamowienie).raises(ValueError).when_called_with(Storage_Base.zamowienia[0].id)

    def test_storage_add_item(self):
        przedmiot = Przedmiot(12, "Nazwa", 100.0)
        self.item_storage.dodaj_przedmiot(przedmiot)
        assert_that(Storage_Base.przedmioty).contains(przedmiot)

    @patch.object(Baza_Danych, 'dodaj_przedmiot')
    def test_storage_add_item_database_check(self, mock_dodaj_przedmiot):
        przedmiot = Przedmiot(12, "Nazwa", 100.0)
        self.item_storage.dodaj_przedmiot(przedmiot)
        mock_dodaj_przedmiot.assert_called_once_with(przedmiot.id, przedmiot.nazwa, przedmiot.wartosc)

    def test_storage_add_item_already_exists(self):
        assert_that(self.item_storage.dodaj_przedmiot).raises(ValueError).when_called_with(Storage_Base.przedmioty[0].id)

    @patch.object(Baza_Danych, 'usun_klienta')
    def test_storage_remove_client(self, mock_usun_klienta):
        self.client_storage.usun_klienta(Storage_Base.klienci[0].id)
        assert_that(Storage_Base.klienci).is_empty()

    @patch.object(Baza_Danych, 'usun_klienta')
    def test_storage_remove_client_database_check(self, mock_usun_klienta):
        id = Storage_Base.klienci[0].id
        self.client_storage.usun_klienta(id)
        mock_usun_klienta.assert_called_once_with(id)
        
    def test_storage_remove_client_not_found(self):
        assert_that(self.client_storage.usun_klienta).raises(ValueError).when_called_with(12)

    @patch.object(Baza_Danych, 'usun_zamowienie')
    def test_storage_remove_order(self, mock_usun_zamowienie):
        self.order_storage.usun_zamowienie(Storage_Base.zamowienia[0].id)
        assert_that(Storage_Base.zamowienia).is_empty()

    @patch.object(Baza_Danych, 'usun_zamowienie')
    def test_storage_remove_order_database_check(self, mock_usun_zamowienie):
        id = Storage_Base.zamowienia[0].id
        self.order_storage.usun_zamowienie(id)
        mock_usun_zamowienie.assert_called_once_with(id)

    def test_storage_remove_order_not_found(self):
        assert_that(self.order_storage.usun_zamowienie).raises(ValueError).when_called_with(12)

    @patch.object(Baza_Danych, 'usun_przedmiot')
    def test_storage_remove_item(self, mock_usun_przedmiot):
        self.item_storage.usun_przedmiot(Storage_Base.przedmioty[0].id)
        assert_that(Storage_Base.przedmioty).is_empty()

    @patch.object(Baza_Danych, 'usun_przedmiot')
    def test_storage_remove_item_database_check(self, mock_usun_przedmiot):
        id = Storage_Base.przedmioty[0].id
        self.item_storage.usun_przedmiot(id)
        mock_usun_przedmiot.assert_called_once_with(id)

    def test_storage_remove_item_not_found(self):
        assert_that(self.item_storage.usun_przedmiot).raises(ValueError).when_called_with(12)

    def test_storage_get_clients(self):
        assert_that(self.client_storage.dane_klienci()).contains((Storage_Base.klienci[0].id, Storage_Base.klienci[0].imie, Storage_Base.klienci[0].nazwisko, Storage_Base.klienci[0].email))

    def test_storage_get_orders(self):
        assert_that(self.order_storage.dane_zamowienia()).contains((Storage_Base.zamowienia[0].id, Storage_Base.zamowienia[0].klient_id))

    def test_storage_get_items(self):
        assert_that(self.item_storage.dane_przedmioty()).contains((Storage_Base.przedmioty[0].id, Storage_Base.przedmioty[0].nazwa, Storage_Base.przedmioty[0].wartosc))

    def test_storage_find_client(self):
        assert_that(self.client_storage.znajdz_klienta(Storage_Base.klienci[0].id)).is_instance_of(Klient)

    def test_storage_find_client_not_found(self):
        assert_that(self.client_storage.znajdz_klienta(12)).is_none()

    def test_storage_find_order(self):
        assert_that(self.order_storage.znajdz_zamowienie(Storage_Base.zamowienia[0].id)).is_instance_of(Zamowienie)

    def test_storage_find_order_not_found(self):
        assert_that(self.order_storage.znajdz_zamowienie(2)).is_none()

    def test_storage_find_item(self):
        assert_that(self.item_storage.znajdz_przedmiot(Storage_Base.przedmioty[0].id)).is_instance_of(Przedmiot)

    def test_storage_find_item_not_found(self):
        assert_that(self.item_storage.znajdz_przedmiot(112)).is_none()

    # @patch.object(Baza_Danych, 'znajdz_klienta', return_value=(11, "Jan", "Kowalski", "mail"))
    # @patch.object(Baza_Danych, 'czytaj_klientow', return_value=[(11, "Jan", "Kowalski", "mail")])
    # @patch.object(Baza_Danych, 'czytaj_zamowienia', return_value=[(1, 11)])
    # @patch.object(Baza_Danych, 'czytaj_przedmioty_z_zamowien', return_value=[(1, 111)])
    # @patch.object(Baza_Danych, 'czytaj_przedmioty', return_value=[(111, "Nazwa", 100.0)])
    # def test_storage_import_from_database_client_check(self, mock_czytaj_przedmioty, mock_czytaj_przedmioty_z_zamowien, mock_czytaj_zamowienia, mock_czytaj_klientow, mock_znajdz_klienta):
    #     Storage_Base.importuj_z_bazy()
    #     mock_czytaj_klientow.assert_called_once()

    # @patch.object(Baza_Danych, 'znajdz_klienta', return_value=(11, "Jan", "Kowalski", "mail"))
    # @patch.object(Baza_Danych, 'czytaj_klientow', return_value=[(11, "Jan", "Kowalski", "mail")])
    # @patch.object(Baza_Danych, 'czytaj_zamowienia', return_value=[(1, 11)])
    # @patch.object(Baza_Danych, 'czytaj_przedmioty_z_zamowien', return_value=[(1, 111)])
    # @patch.object(Baza_Danych, 'czytaj_przedmioty', return_value=[(111, "Nazwa", 100.0)])
    # def test_storage_import_from_database_zamowienia_check(self, mock_czytaj_przedmioty, mock_czytaj_przedmioty_z_zamowien, mock_czytaj_zamowienia, mock_czytaj_klientow, mock_znajdz_klienta):
    #     Storage_Base.importuj_z_bazy()
    #     mock_czytaj_zamowienia.assert_called_once()

    # @patch.object(Baza_Danych, 'znajdz_klienta', return_value=(11, "Jan", "Kowalski", "mail"))
    # @patch.object(Baza_Danych, 'czytaj_klientow', return_value=[(11, "Jan", "Kowalski", "mail")])
    # @patch.object(Baza_Danych, 'czytaj_zamowienia', return_value=[(1, 11)])
    # @patch.object(Baza_Danych, 'czytaj_przedmioty_z_zamowien', return_value=[(1, 111)])
    # @patch.object(Baza_Danych, 'czytaj_przedmioty', return_value=[(111, "Nazwa", 100.0)])
    # def test_storage_import_from_database_item_check(self, mock_czytaj_przedmioty, mock_czytaj_przedmioty_z_zamowien, mock_czytaj_zamowienia, mock_czytaj_klientow, mock_znajdz_klienta):
    #     Storage_Base.importuj_z_bazy()
    #     mock_czytaj_przedmioty.assert_called_once()

    # @patch.object(Baza_Danych, 'znajdz_klienta', return_value=(11, "Jan", "Kowalski", "mail"))
    # @patch.object(Baza_Danych, 'czytaj_klientow', return_value=[(11, "Jan", "Kowalski", "mail")])
    # @patch.object(Baza_Danych, 'czytaj_zamowienia', return_value=[(1, 11)])
    # @patch.object(Baza_Danych, 'czytaj_przedmioty_z_zamowien', return_value=[(1, 111)])
    # @patch.object(Baza_Danych, 'czytaj_przedmioty', return_value=[(111, "Nazwa", 100.0)])
    # def test_storage_import_from_database_relations_check(self, mock_czytaj_przedmioty, mock_czytaj_przedmioty_z_zamowien, mock_czytaj_zamowienia, mock_czytaj_klientow, mock_znajdz_klienta):
    #     Storage_Base.importuj_z_bazy()
    #     mock_czytaj_przedmioty_z_zamowien.assert_called_once()



    def tearDown(self):
        del self.client_storage
        del self.order_storage
        del self.item_storage