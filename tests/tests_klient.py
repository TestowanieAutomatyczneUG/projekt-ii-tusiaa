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

    def test_klient_add_order(self):
        self.klient.dodaj_zamowienie(2)
        assert_that(self.klient.zamowienia).contains(2)

    @patch.object(Baza_Danych, 'dodaj_zamowienie')
    def test_klient_add_order_database_check(self, mock_dodaj_zamowienie):
        self.klient.dodaj_zamowienie(2)
        mock_dodaj_zamowienie.assert_called_with(2, self.klient.id)

    def test_klient_remove_order(self):
        self.klient.usun_zamowienie(1)
        assert_that(self.klient.zamowienia).does_not_contain(1)

    @patch.object(Baza_Danych, 'usun_zamowienie')
    def test_klient_remove_order_database_check(self, mock_usun_zamowienie):
        self.klient.usun_zamowienie(1)
        mock_usun_zamowienie.assert_called_with(1)

    def test_klient_remove_order_not_found(self):
        assert_that(self.klient.usun_zamowienie).raises(ValueError).when_called_with(2)


