from models.autokolcsonzo import Autokolcsonzo
from models.szemelyauto import Szemelyauto
from models.teherauto import Teherauto
from models.berles import Berles


def rendszer_feltoltes():

    kolcsonzo = Autokolcsonzo("SpeedCar Autókölcsönző")

    auto1 = Szemelyauto("ABC-123", "Toyota Corolla", 12000, 5)
    auto2 = Szemelyauto("XYZ-456", "Honda Civic", 14000, 5)
    auto3 = Teherauto("TRK-999", "Ford Transit", 20000, 3500)

    kolcsonzo.auto_hozzaadas(auto1)
    kolcsonzo.auto_hozzaadas(auto2)
    kolcsonzo.auto_hozzaadas(auto3)

    kolcsonzo.berles_hozzaadas(
        Berles(auto1, "2026-05-20", "Kiss Péter")
    )

    kolcsonzo.berles_hozzaadas(
        Berles(auto2, "2026-05-21", "Nagy Anna")
    )

    kolcsonzo.berles_hozzaadas(
        Berles(auto3, "2026-05-22", "Szabó László")
    )

    kolcsonzo.berles_hozzaadas(
        Berles(auto1, "2026-05-23", "Tóth Márk")
    )

    return kolcsonzo