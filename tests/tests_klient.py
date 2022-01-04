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

    
