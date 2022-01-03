import unittest
from assertpy import *
from parameterized import *
from unittest.mock import *
from src.przedmiot import *

@parameterized_class(('str_wrong_value', 'int_wrong_value', 'positive_float_wrong_value'), [
    (1, "int", -5.0),
    (1.5, 1.5, "float"),
    (True, True, True),
    (None, None, None),
    ("", "", ""),
    ([1,2,3], [1,2,3], [1,2,3]),
    ({'name': 2, 'grades': 4}, {'name': 2, 'grades': 4}, {'name': 2, 'grades': 4}),
])
class TestsParametrizedPrzedmiot(unittest.TestCase):

    @patch.object(Baza_Danych, 'czytaj_przedmioty', return_value=[(1, "Nazwa", 100.0)])
    def setUp(self, mock_czytaj_przedmioty):
        self.przedmiot = Przedmiot(mock_czytaj_przedmioty()[0][0], mock_czytaj_przedmioty()[0][1], mock_czytaj_przedmioty()[0][2])

    def test_przedmiot_init_wrong_id(self):
        assert_that(Przedmiot).raises(ValueError).when_called_with(self.int_wrong_value, self.przedmiot.nazwa, self.przedmiot.wartosc)

    def test_przedmiot_init_wrong_nazwa(self):
        assert_that(Przedmiot).raises(ValueError).when_called_with(self.przedmiot.id, self.str_wrong_value, self.przedmiot.wartosc)

    def test_przedmiot_init_wrong_wartosc(self):
        assert_that(Przedmiot).raises(ValueError).when_called_with(self.przedmiot.id, self.przedmiot.nazwa, self.positive_float_wrong_value)
