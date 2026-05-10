from models.auto import Auto


class Szemelyauto(Auto):

    def __init__(self, rendszam: str, tipus: str, berleti_dij: int, ajtok_szama: int):
        super().__init__(rendszam, tipus, berleti_dij)
        self._ajtok_szama = ajtok_szama

    def __str__(self):
        return f"Személyautó | {super().__str__()} | Ajtók száma: {self._ajtok_szama}"