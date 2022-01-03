from src.baza_danych import Baza_Danych

class Przedmiot:
    def __init__(self, id: int, nazwa: str, wartosc: float):
        if type(id) is not int:
            raise ValueError("id musi być liczbą")
        if type(nazwa) is not str or not nazwa:
            raise ValueError("nazwa musi być napisem")
        if type(wartosc) is not float and type(wartosc) is not int:
            raise ValueError("wartość musi być liczbą")
        if wartosc < 0:
            raise ValueError("wartość musi być dodatnia")
        self.id = id
        self.nazwa = nazwa
        self.wartosc = float(wartosc)

        