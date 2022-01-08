import unittest
from assertpy import *
from unittest.mock import *
from src.klient import *

class TestsKlient(unittest.TestCase):

    @patch.object(Baza_Danych, 'czytaj_klientow', return_value=[(11, "Jan", "Kowalski", "mail")])
    @patch.object(Baza_Danych, 'znajdz_zamowienia_klienta', return_value=[(1, 11)])
    def setUp(self, mock_znajdz_zamowienia_klienta, mock_czytaj_klientow):
        self.klient = Klient(mock_czytaj_klientow()[0][0], mock_czytaj_klientow()[0][1], mock_czytaj_klientow()[0][2], mock_czytaj_klientow()[0][3])
        zamowienie = mock_znajdz_zamowienia_klienta(mock_czytaj_klientow()[0][0])[0]
        self.klient.zamowienia.append(zamowienie[0])

    def test_klient_init(self):
        assert_that(self.klient).is_not_none()

    @patch.object(Baza_Danych, 'znajdz_zamowienie', return_value=None)
    def test_klient_add_order(self, mock_znajdz_zamowienie):
        self.klient.dodaj_zamowienie(2)
        assert_that(self.klient.zamowienia).contains(2)

    @patch.object(Baza_Danych, 'znajdz_zamowienie', return_value=None)
    @patch.object(Baza_Danych, 'dodaj_zamowienie')
    def test_klient_add_order_database_check(self, mock_dodaj_zamowienie, mock_znajdz_zamowienie):
        self.klient.dodaj_zamowienie(2)
        mock_dodaj_zamowienie.assert_called_with(2, self.klient.id)

    @patch.object(Baza_Danych, 'znajdz_zamowienie', return_value=(1, 11))
    def test_klient_add_order_already_exists(self, mock_znajdz_zamowienie):
        assert_that(self.klient.dodaj_zamowienie).raises(ValueError).when_called_with(1)

    def test_klient_remove_order(self):
        self.klient.usun_zamowienie(1)
        assert_that(self.klient.zamowienia).does_not_contain(1)

    @patch.object(Baza_Danych, 'usun_zamowienie')
    def test_klient_remove_order_database_check(self, mock_usun_zamowienie):
        self.klient.usun_zamowienie(1)
        mock_usun_zamowienie.assert_called_with(1)

    def test_klient_remove_order_not_found(self):
        assert_that(self.klient.usun_zamowienie).raises(ValueError).when_called_with(2)

    def test_klient_change_name(self):
        self.klient.zmien_imie("Janusz")
        assert_that(self.klient.imie).is_equal_to("Janusz")

    def test_klient_change_surname(self):
        self.klient.zmien_nazwisko("Nowak")
        assert_that(self.klient.nazwisko).is_equal_to("Nowak")

    def test_klient_change_email(self):
        self.klient.zmien_email("test.email")
        assert_that(self.klient.email).is_equal_to("test.email")

    @patch.object(Baza_Danych, 'edytuj_klienta')
    def test_klient_change_name_database_check(self, mock_edytuj_klienta):
        self.klient.zmien_imie("Janusz")
        mock_edytuj_klienta.assert_called_with(self.klient.id, "Janusz", self.klient.nazwisko, self.klient.email)

    @patch.object(Baza_Danych, 'edytuj_klienta')
    def test_klient_change_surname_database_check(self, mock_edytuj_klienta):
        self.klient.zmien_nazwisko("Nowak")
        mock_edytuj_klienta.assert_called_with(self.klient.id, self.klient.imie, "Nowak", self.klient.email)

    @patch.object(Baza_Danych, 'edytuj_klienta')
    def test_klient_change_email_database_check(self, mock_edytuj_klienta):
        self.klient.zmien_email("test.email")
        mock_edytuj_klienta.assert_called_with(self.klient.id, self.klient.imie, self.klient.nazwisko, "test.email")

    @patch.object(Baza_Danych, 'znajdz_przedmioty_z_zamowienia', return_value=[(1, 111), (1, 222)])
    @patch.object(Baza_Danych, 'znajdz_przedmiot', side_effect=[(111, "Nazwa", 100.0), (222, "Nazwa2", 200.0)])
    def test_klient_get_orders(self, mock_znajdz_przedmiot, mock_znajdz_zamowienie):
        assert_that(self.klient.dane_zamowienia()).contains([(111, "Nazwa", 100.0), (222, "Nazwa2", 200.0)])
        
    @patch.object(Baza_Danych, 'znajdz_przedmioty_z_zamowienia', return_value=[(1, 111), (1, 222)])
    @patch.object(Baza_Danych, 'znajdz_przedmiot', side_effect=[(111, "Nazwa", 100.0), (222, "Nazwa2", 200.0)])
    def test_klient_get_orders_database_check(self, mock_znajdz_przedmiot, mock_znajdz_zamowienie):
        self.klient.dane_zamowienia()
        mock_znajdz_zamowienie.assert_called_with(1)

    def tearDown(self):
        del self.klient