import unittest
from assertpy import *
from unittest.mock import *
from src.przedmiot import *

class TestsPrzedmiot(unittest.TestCase):

    @patch.object(Baza_Danych, 'czytaj_przedmioty', return_value=[(1, "Nazwa", 100.0)])
    def setUp(self, mock_czytaj_przedmioty):
        self.przedmiot = Przedmiot(mock_czytaj_przedmioty()[0][0], mock_czytaj_przedmioty()[0][1], mock_czytaj_przedmioty()[0][2])

    def test_przedmiot_init(self):
        assert_that(self.przedmiot).is_not_none()
    
    

