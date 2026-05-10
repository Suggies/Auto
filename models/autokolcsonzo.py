from models.berles import Berles


class Autokolcsonzo:

    def __init__(self, nev: str):
        self._nev = nev
        self._autok = []
        self._berlesek = []

    def auto_hozzaadas(self, auto):
        self._autok.append(auto)

    def berles_hozzaadas(self, berles: Berles):
        self._berlesek.append(berles)

    def autok_listazasa(self):
        if not self._autok:
            print("Nincs elérhető autó.")
            return

        for index, auto in enumerate(self._autok, start=1):
            print(f"{index}. {auto}")

    def berlesek_listazasa(self):
        if not self._berlesek:
            print("Nincsenek aktív bérlések.")
            return

        for index, berles in enumerate(self._berlesek, start=1):
            print(f"{index}. {berles}")

    def auto_berlese(self, rendszam: str, datum: str, berlo_nev: str):

        for berles in self._berlesek:
            if berles.auto.rendszam == rendszam and berles.datum == datum:
                raise Exception("Az autó már foglalt erre a napra.")

        auto = None

        for jarmu in self._autok:
            if jarmu.rendszam == rendszam:
                auto = jarmu
                break

        if auto is None:
            raise Exception("Nem létező rendszám.")

        uj_berles = Berles(auto, datum, berlo_nev)

        if not uj_berles.ervenyes_datum():
            raise ValueError("Hibás dátumformátum. Helyes formátum: ÉÉÉÉ-HH-NN")

        self._berlesek.append(uj_berles)

        return auto.berleti_dij

    def berles_lemondasa(self, rendszam: str, datum: str):

        for berles in self._berlesek:
            if berles.auto.rendszam == rendszam and berles.datum == datum:
                self._berlesek.remove(berles)
                return True

        raise Exception("Nincs ilyen bérlés.")