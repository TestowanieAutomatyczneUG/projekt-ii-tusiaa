import unittest
from assertpy import *
from parameterized import *
from unittest.mock import *
from src.zamowienie import *

@parameterized_class(('str_wrong_value', 'int_wrong_value', 'positive_float_wrong_value'), [
    (1, "int", -5.0),
    (1.5, 1.5, "float"),
    (True, True, True),
    (None, None, None),
    ("", "", ""),
    ([1,2,3], [1,2,3], [1,2,3]),
    ({'name': 2, 'grades': 4}, {'name': 2, 'grades': 4}, {'name': 2, 'grades': 4}),
])
class TestsParametrizedZamowienie(unittest.TestCase):

    @patch.object(Baza_Danych, 'czytaj_zamowienia', return_value=[(1, 11)])
    @patch.object(Baza_Danych, 'znajdz_przedmioty_z_zamowienia', return_value=[(1, 111)])
    @patch.object(Baza_Danych, 'znajdz_przedmiot', return_value=(111, "Nazwa", 100.0))
    def setUp(self, mock_znajdz_przedmiot, mock_znajdz_przedmioty_z_zamowienia, mock_czytaj_zamowienia):
        self.zamowienie = Zamowienie(mock_czytaj_zamowienia()[0][0], mock_czytaj_zamowienia()[0][1])
        przedmiot = mock_znajdz_przedmiot(mock_znajdz_przedmioty_z_zamowienia(mock_czytaj_zamowienia()[0][0])[0][1])
        self.zamowienie.przedmioty.append(Przedmiot(przedmiot[0], przedmiot[1], przedmiot[2]))

    def test_zamowienie_init_wrong_id(self):
        assert_that(Zamowienie).raises(ValueError).when_called_with(self.int_wrong_value, self.zamowienie.klient_id)

    def test_zamowienie_init_wrong_klient_id(self):
        assert_that(Zamowienie).raises(ValueError).when_called_with(self.zamowienie.id, self.int_wrong_value)