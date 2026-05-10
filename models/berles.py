from datetime import datetime


class Berles:

    def __init__(self, auto, datum: str, berlo_nev: str):
        self._auto = auto
        self._datum = datum
        self._berlo_nev = berlo_nev

    @property
    def auto(self):
        return self._auto

    @property
    def datum(self):
        return self._datum

    @property
    def berlo_nev(self):
        return self._berlo_nev

    def ervenyes_datum(self):
        try:
            datetime.strptime(self._datum, "%Y-%m-%d")
            return True
        except ValueError:
            return False

    def __str__(self):
        return (
            f"Bérlő: {self.berlo_nev} | "
            f"Autó: {self.auto.tipus} ({self.auto.rendszam}) | "
            f"Dátum: {self.datum}"
        )