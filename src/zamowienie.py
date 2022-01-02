from src.baza_danych import Baza_Danych

class Zamowienie:
    def __init__(self, id):
        self.id = id
        self.przedmioty = []