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

    @patch.object(Baza_Danych, 'dodaj_przedmiot')
    def test_przedmiot_add_item_to_database(self, mock_dodaj_przedmiot):
        self.przedmiot.dodaj_do_bazy()
        mock_dodaj_przedmiot.assert_called_once_with(self.przedmiot.id, self.przedmiot.nazwa, self.przedmiot.wartosc)

    @patch.object(Baza_Danych, 'dodaj_przedmiot', side_effect=[None, ValueError])
    def test_przedmiot_add_item_to_database_already_exists(self, mock_dodaj_przedmiot):
        self.przedmiot.dodaj_do_bazy()
        assert_that(self.przedmiot.dodaj_do_bazy).raises(ValueError)

    @patch.object(Baza_Danych, 'edytuj_przedmiot')
    def test_przedmiot_change_name(self, mock_edytuj_przedmiot):
        self.przedmiot.zmien_nazwe("Nowa nazwa")
        mock_edytuj_przedmiot.assert_called_once_with(self.przedmiot.id, "Nowa nazwa", self.przedmiot.wartosc)

    @patch.object(Baza_Danych, 'edytuj_przedmiot')
    def test_przedmiot_change_value_float(self, mock_edytuj_przedmiot):
        self.przedmiot.zmien_wartosc(200.99)
        mock_edytuj_przedmiot.assert_called_once_with(self.przedmiot.id, self.przedmiot.nazwa, 200.99)

    @patch.object(Baza_Danych, 'edytuj_przedmiot')
    def test_przedmiot_change_value_int(self, mock_edytuj_przedmiot):
        self.przedmiot.zmien_wartosc(200)
        mock_edytuj_przedmiot.assert_called_once_with(self.przedmiot.id, self.przedmiot.nazwa, float(200))
    

