import unittest
from assertpy import *
from unittest.mock import *
from src.storage import *

class TestsStorage(unittest.TestCase):

    @patch.object(Baza_Danych, 'znajdz_klienta', return_value=(11, "Jan", "Kowalski", "mail"))
    @patch.object(Baza_Danych, 'czytaj_klientow', return_value=[(11, "Jan", "Kowalski", "mail")])
    @patch.object(Baza_Danych, 'czytaj_zamowienia', return_value=[(1, 11)])
    @patch.object(Baza_Danych, 'czytaj_przedmioty_z_zamowien', return_value=[(1, 111)])
    @patch.object(Baza_Danych, 'czytaj_przedmioty', return_value=[(111, "Nazwa", 100.0)])
    def setUp(self, mock_czytaj_przedmioty, mock_czytaj_przedmioty_z_zamowien, mock_czytaj_zamowienia, mock_czytaj_klientow, mock_znajdz_klienta):
        self.storage = Storage()
        self.storage.klienci.append(Klient(mock_czytaj_klientow()[0][0], mock_czytaj_klientow()[0][1], mock_czytaj_klientow()[0][2], mock_czytaj_klientow()[0][3]))
        self.storage.zamowienia.append(Zamowienie(mock_czytaj_zamowienia()[0][0], mock_czytaj_zamowienia()[0][1]))
        self.storage.przedmioty.append(Przedmiot(mock_czytaj_przedmioty()[0][0], mock_czytaj_przedmioty()[0][1], mock_czytaj_przedmioty()[0][2]))
        self.storage.przedmioty_w_zamowieniach.append(mock_czytaj_przedmioty_z_zamowien()[0])

    def test_storage_init(self):
        assert_that(self.storage).is_not_none()

    @patch.object(Baza_Danych, 'dodaj_klienta')
    def test_storage_add_client(self, mock_dodaj_klienta):
        klient = Klient(12, "Jan", "Kowalski", "mail")
        self.storage.dodaj_klienta(klient)
        assert_that(self.storage.klienci).contains(klient)

    @patch.object(Baza_Danych, 'dodaj_klienta')
    def test_storage_add_client_database_check(self, mock_dodaj_klienta):
        klient = Klient(12, "Jan", "Kowalski", "mail")
        self.storage.dodaj_klienta(klient)
        mock_dodaj_klienta.assert_called_once_with(klient.id, klient.imie, klient.nazwisko, klient.email)

    @patch.object(Baza_Danych, 'dodaj_klienta')
    def test_storage_add_client_already_exists(self, mock_dodaj_klienta):
        assert_that(self.storage.dodaj_klienta).raises(ValueError).when_called_with(self.storage.klienci[0].id)

    @patch.object(Baza_Danych, 'znajdz_klienta', return_value=(11, "Jan", "Kowalski", "mail"))
    @patch.object(Baza_Danych, 'dodaj_zamowienie')
    def test_storage_add_order(self, mock_dodaj_zamowienie, mock_znajdz_klienta):
        zamowienie = Zamowienie(2, 11)
        self.storage.dodaj_zamowienie(zamowienie)
        assert_that(self.storage.zamowienia).contains(zamowienie)

    @patch.object(Baza_Danych, 'znajdz_klienta', return_value=(11, "Jan", "Kowalski", "mail"))
    @patch.object(Baza_Danych, 'dodaj_zamowienie')
    def test_storage_add_order_database_check(self, mock_dodaj_zamowienie, mock_znajdz_klienta):
        zamowienie = Zamowienie(2, 11)
        self.storage.dodaj_zamowienie(zamowienie)
        mock_dodaj_zamowienie.assert_called_once_with(zamowienie.id, zamowienie.klient_id)

    def test_storage_add_order_already_exists(self):
        assert_that(self.storage.dodaj_zamowienie).raises(ValueError).when_called_with(self.storage.zamowienia[0].id)

    def test_storage_add_item(self):
        przedmiot = Przedmiot(12, "Nazwa", 100.0)
        self.storage.dodaj_przedmiot(przedmiot)
        assert_that(self.storage.przedmioty).contains(przedmiot)

    @patch.object(Baza_Danych, 'dodaj_przedmiot')
    def test_storage_add_item_database_check(self, mock_dodaj_przedmiot):
        przedmiot = Przedmiot(12, "Nazwa", 100.0)
        self.storage.dodaj_przedmiot(przedmiot)
        mock_dodaj_przedmiot.assert_called_once_with(przedmiot.id, przedmiot.nazwa, przedmiot.cena)

    def test_storage_add_item_already_exists(self):
        assert_that(self.storage.dodaj_przedmiot).raises(ValueError).when_called_with(self.storage.przedmioty[0].id)

    @patch.object(Baza_Danych, 'usun_klienta')
    def test_storage_remove_client(self, mock_usun_klienta):
        self.storage.usun_klienta(self.storage.klienci[0].id)
        assert_that(self.storage.klienci).is_empty()

    @patch.object(Baza_Danych, 'usun_klienta')
    def test_storage_remove_client_database_check(self, mock_usun_klienta):
        id = self.storage.klienci[0].id
        self.storage.usun_klienta(id)
        mock_usun_klienta.assert_called_once_with(id)
        
    def test_storage_remove_client_not_found(self):
        assert_that(self.storage.usun_klienta).raises(ValueError).when_called_with(12)

    def test_storage_get_clients(self):
        assert_that(self.storage.dane_klienci()).contains((self.storage.klienci[0].id, self.storage.klienci[0].imie, self.storage.klienci[0].nazwisko, self.storage.klienci[0].email))

    def test_storage_get_orders(self):
        assert_that(self.storage.dane_zamowienia()).contains((self.storage.zamowienia[0].id, self.storage.zamowienia[0].klient_id))

    def test_storage_get_items(self):
        assert_that(self.storage.dane_przedmioty()).contains((self.storage.przedmioty[0].id, self.storage.przedmioty[0].nazwa, self.storage.przedmioty[0].wartosc))

    def test_storage_find_client(self):
        assert_that(self.storage.znajdz_klienta(self.storage.klienci[0].id)).is_instance_of(Klient)

    def test_storage_find_client_not_found(self):
        assert_that(self.storage.znajdz_klienta(12)).is_none()

    def test_storage_find_order(self):
        assert_that(self.storage.znajdz_zamowienie(self.storage.zamowienia[0].id)).is_instance_of(Zamowienie)

    def test_storage_find_order_not_found(self):
        assert_that(self.storage.znajdz_zamowienie(2)).is_none()

    def test_storage_find_item(self):
        assert_that(self.storage.znajdz_przedmiot(self.storage.przedmioty[0].id)).is_instance_of(Przedmiot)

    def test_storage_find_item_not_found(self):
        assert_that(self.storage.znajdz_przedmiot(112)).is_none()

    def tearDown(self):
        del self.storage