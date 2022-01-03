import unittest
from assertpy import *
from unittest.mock import *
from src.zamowienie import *

class TestsZamowienie(unittest.TestCase):

    @patch.object(Baza_Danych, 'czytaj_zamowienia', return_value=[(1, 11)])
    @patch.object(Baza_Danych, 'znajdz_przedmioty_z_zamowienia', return_value=[(1, 111)])
    @patch.object(Baza_Danych, 'znajdz_przedmiot', return_value=(111, "Nazwa", 100.0))
    def setUp(self, mock_czytaj_zamowienia, mock_znajdz_przedmioty_z_zamowienia, mock_znajdz_przedmiot):
        self.zamowienie = Zamowienie(mock_czytaj_zamowienia()[0][0], mock_czytaj_zamowienia()[0][1])
        przedmiot = mock_znajdz_przedmiot(mock_znajdz_przedmioty_z_zamowienia(mock_czytaj_zamowienia()[0][0])[0][1])
        self.zamowienie.przedmioty.append(Przedmiot(przedmiot[0], przedmiot[1], przedmiot[2]))
            
    def test_zamowienie_init(self):
        assert_that(self.zamowienie).is_not_none()


