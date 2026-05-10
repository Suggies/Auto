from models.auto import Auto


class Teherauto(Auto):

    def __init__(self, rendszam: str, tipus: str, berleti_dij: int, teherbiras: int):
        super().__init__(rendszam, tipus, berleti_dij)
        self._teherbiras = teherbiras

    def __str__(self):
        return f"Teherautó | {super().__str__()} | Teherbírás: {self._teherbiras} kg"