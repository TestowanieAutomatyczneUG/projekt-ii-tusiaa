import unittest
from assertpy import *
from parameterized import *
from unittest.mock import *
from src.storage import *

@parameterized_class(('str_wrong_value', 'int_wrong_value', 'class_wrong_value'), [
    (1, "int", 5.0),
    (1, "int", 5),
    (1.5, 1.5, "class"),
    (True, True, True),
    (None, None, None),
    ("", "", ""),
    ([1,2,3], [1,2,3], [1,2,3]),
    ({'name': 2, 'grades': 4}, {'name': 2, 'grades': 4}, {'name': 2, 'grades': 4}),
])
class TestsParametrizedStorage(unittest.TestCase):

    @patch.object(Baza_Danych, 'czytaj_klientow', return_value=[(11, "Jan", "Kowalski", "mail")])
    @patch.object(Baza_Danych, 'czytaj_zamowienia', return_value=[(1, 11)])
    @patch.object(Baza_Danych, 'czytaj_przedmioty_z_zamowien', return_value=[(1, 111)])
    @patch.object(Baza_Danych, 'czytaj_przedmioty', return_value=[(111, "Nazwa", 100.0)])
    def setUp(self, mock_czytaj_przedmioty, mock_czytaj_przedmioty_z_zamowien, mock_czytaj_zamowienia, mock_czytaj_klientow):
        self.storage = Storage()
        self.storage.klienci.append(mock_czytaj_klientow()[0])
        self.storage.zamowienia.append(mock_czytaj_zamowienia()[0])
        self.storage.przedmioty.append(mock_czytaj_przedmioty()[0])
        self.storage.przedmioty_w_zamowieniach.append(mock_czytaj_przedmioty_z_zamowien()[0])








    def tearDown(self):
        del self.storage