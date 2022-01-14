import unittest
from assertpy import *
from unittest.mock import *
from src.zamowienie import *

class TestsZamowienie(unittest.TestCase):

    @patch.object(Baza_Danych, 'czytaj_zamowienia', return_value=[(1, 11)])
    @patch.object(Baza_Danych, 'znajdz_klienta', return_value=(11, "Jan", "Kowalski", "mail"))
    @patch.object(Baza_Danych, 'znajdz_przedmiot', return_value=(111, "Nazwa", 100.0))
    def setUp(self, mock_znajdz_przedmiot, mock_znajdz_klienta, mock_czytaj_zamowienia):
        self.zamowienie = Zamowienie(mock_czytaj_zamowienia()[0][0], mock_czytaj_zamowienia()[0][1])
        przedmiot = Przedmiot(mock_znajdz_przedmiot()[0], mock_znajdz_przedmiot()[1], mock_znajdz_przedmiot()[2])
        self.zamowienie.przedmioty.append(przedmiot)
            
    def test_zamowienie_init(self):
        assert_that(self.zamowienie).is_not_none()

    @patch.object(Baza_Danych, 'znajdz_klienta', return_value=None)
    def test_zamowienie_init_client_not_found(self, mock_znajdz_klienta):
        assert_that(Zamowienie).raises(ValueError).when_called_with(1, 1)

    @patch.object(Baza_Danych, 'znajdz_przedmiot', return_value=(112, "Nazwa", 100.0))
    def test_zamowienie_add_item(self, mock_znajdz_przedmiot):
        Przedmiot(112, "Nazwa", 100.0)
        self.zamowienie.dodaj_przedmiot(112)
        assert_that(self.zamowienie.przedmioty).is_length(2)

    @patch.object(Baza_Danych, 'znajdz_przedmiot', return_value=(112, "Nazwa", 100.0))
    @patch.object(Baza_Danych, 'dodaj_przedmiot_do_zamowienia')
    def test_zamowienie_add_item_database_check(self, mock_dodaj_przedmiot_do_zamowienia, mock_znajdz_przedmiot):
        Przedmiot(112, "Nazwa", 100.0)
        self.zamowienie.dodaj_przedmiot(112)
        mock_dodaj_przedmiot_do_zamowienia.assert_called_with(self.zamowienie.id, 112)

    @patch.object(Baza_Danych, 'znajdz_przedmiot', return_value=None)
    def test_zamowienie_add_item_not_found(self, mock_znajdz_przedmiot):
        with self.assertRaises(ValueError):
            self.zamowienie.dodaj_przedmiot(112)

    def test_zamowienie_remove_item(self):
        self.zamowienie.usun_przedmiot(self.zamowienie.przedmioty[0].id)
        assert_that(self.zamowienie.przedmioty).is_length(0)

    @patch.object(Baza_Danych, 'usun_przedmiot_z_zamowienia')
    def test_zamowienie_remove_item_database_check(self, mock_usun_przedmiot_z_zamowienia):
        id = self.zamowienie.przedmioty[0].id
        self.zamowienie.usun_przedmiot(id)
        mock_usun_przedmiot_z_zamowienia.assert_called_with(self.zamowienie.id, id)

    def test_zamowienie_remove_item_not_found(self):
        with self.assertRaises(ValueError):
            self.zamowienie.usun_przedmiot(112)

    def test_zamowienie_check_if_item_in_order_true(self):
        assert_that(self.zamowienie.czy_jest_przedmiot(self.zamowienie.przedmioty[0].id)).is_true()

    def test_zamowienie_check_if_item_in_order_false(self):
        assert_that(self.zamowienie.czy_jest_przedmiot(112)).is_false()

    @patch.object(Baza_Danych, 'znajdz_klienta', return_value=(11, "Jan", "Kowalski", "mail"))
    def test_zamowienie_get_client(self, mock_znajdz_klienta):
        self.zamowienie.dane_klient()
        mock_znajdz_klienta.assert_called_once()

    def test_zamowienie_get_items(self):
        assert_that(self.zamowienie.dane_przedmioty()).contains((111, "Nazwa", 100.0))

    def test_zamowienie_get_items_empty(self):
        self.zamowienie.usun_przedmiot(self.zamowienie.przedmioty[0].id)
        assert_that(self.zamowienie.dane_przedmioty()).is_empty()

    def test_zamowienie_get_orders(self):
        assert_that(Zamowienie.wszystkie_zamowienia()).contains(self.zamowienie)

    def test_zamowienie_get_orders_empty(self):
        Zamowienie.zamowienia = []
        assert_that(Zamowienie.wszystkie_zamowienia()).is_empty()

    def tearDown(self):
        del self.zamowienie