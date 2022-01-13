import unittest
from assertpy import *
from parameterized import *
from unittest.mock import *
from src.storage.client_storage import *
from src.storage.order_storage import *
from src.storage.item_storage import *
from src.storage.storage_base import *

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

    @patch.object(Baza_Danych, 'znajdz_klienta', return_value=(11, "Jan", "Kowalski", "mail"))
    @patch.object(Baza_Danych, 'czytaj_klientow', return_value=[(11, "Jan", "Kowalski", "mail")])
    @patch.object(Baza_Danych, 'czytaj_zamowienia', return_value=[(1, 11)])
    @patch.object(Baza_Danych, 'czytaj_przedmioty_z_zamowien', return_value=[(1, 111)])
    @patch.object(Baza_Danych, 'czytaj_przedmioty', return_value=[(111, "Nazwa", 100.0)])
    def setUp(self, mock_czytaj_przedmioty, mock_czytaj_przedmioty_z_zamowien, mock_czytaj_zamowienia, mock_czytaj_klientow, mock_znajdz_klienta):
        self.storage = Storage_Base()
        self.storage.klienci = [Klient(mock_czytaj_klientow()[0][0], mock_czytaj_klientow()[0][1], mock_czytaj_klientow()[0][2], mock_czytaj_klientow()[0][3])]
        self.storage.zamowienia = [Zamowienie(mock_czytaj_zamowienia()[0][0], mock_czytaj_zamowienia()[0][1])]
        self.storage.przedmioty = [Przedmiot(mock_czytaj_przedmioty()[0][0], mock_czytaj_przedmioty()[0][1], mock_czytaj_przedmioty()[0][2])]
        self.storage.przedmioty_w_zamowieniach = [(mock_czytaj_przedmioty_z_zamowien()[0][0], mock_czytaj_przedmioty_z_zamowien()[0][1])]
        self.client_storage = Client_Storage()
        self.order_storage = Order_Storage()
        self.item_storage = Item_Storage()

    def test_storage_add_client_wrong(self):
        assert_that(self.client_storage.dodaj_klienta).raises(ValueError).when_called_with(self.class_wrong_value)

    def test_storage_add_order_wrong(self):
        assert_that(self.order_storage.dodaj_zamowienie).raises(ValueError).when_called_with(self.class_wrong_value)

    def test_storage_add_item_wrong(self):
        assert_that(self.item_storage.dodaj_przedmiot).raises(ValueError).when_called_with(self.class_wrong_value)

    def test_storage_remove_client_wrong(self):
        assert_that(self.client_storage.usun_klienta).raises(ValueError).when_called_with(self.int_wrong_value)

    def test_storage_remove_order_wrong(self):
        assert_that(self.order_storage.usun_zamowienie).raises(ValueError).when_called_with(self.int_wrong_value)

    def test_storage_remove_item_wrong(self):
        assert_that(self.item_storage.usun_przedmiot).raises(ValueError).when_called_with(self.int_wrong_value)

    def test_storage_find_client_wrong(self):
        assert_that(self.client_storage.znajdz_klienta).raises(ValueError).when_called_with(self.int_wrong_value)
    
    def test_storage_find_order_wrong(self):
        assert_that(self.order_storage.znajdz_zamowienie).raises(ValueError).when_called_with(self.int_wrong_value)

    def test_storage_find_item_wrong(self):
        assert_that(self.item_storage.znajdz_przedmiot).raises(ValueError).when_called_with(self.int_wrong_value)






    def tearDown(self):
        del self.storage