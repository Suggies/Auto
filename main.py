from utils.adatfeltoltes import rendszer_feltoltes


def menu():
    print("\n=== AUTÓKÖLCSÖNZŐ RENDSZER ===")
    print("1 - Autók listázása")
    print("2 - Autó bérlése")
    print("3 - Bérlés lemondása")
    print("4 - Bérlések listázása")
    print("0 - Kilépés")


def main():

    kolcsonzo = rendszer_feltoltes()

    while True:

        menu()

        valasztas = input("Válassz menüpontot: ")

        try:

            if valasztas == "1":

                kolcsonzo.autok_listazasa()

            elif valasztas == "2":

                rendszam = input("Rendszám: ")
                datum = input("Dátum (ÉÉÉÉ-HH-NN): ")
                berlo_nev = input("Bérlő neve: ")

                ar = kolcsonzo.auto_berlese(
                    rendszam,
                    datum,
                    berlo_nev
                )

                print(f"Sikeres bérlés. Fizetendő: {ar} Ft")

            elif valasztas == "3":

                rendszam = input("Rendszám: ")
                datum = input("Dátum (ÉÉÉÉ-HH-NN): ")

                kolcsonzo.berles_lemondasa(
                    rendszam,
                    datum
                )

                print("Bérlés sikeresen lemondva.")

            elif valasztas == "4":

                kolcsonzo.berlesek_listazasa()

            elif valasztas == "0":

                print("Kilépés...")
                break

            else:
                print("Érvénytelen menüpont.")

        except Exception as hiba:
            print(f"Hiba: {hiba}")


if __name__ == "__main__":
    main()