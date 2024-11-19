import re
import tkinter as tk
from tkinter import messagebox
import kocka


class Kockadobo:
    """Kockadobásokat kezelő osztály."""

    def __init__(self, dobas_kifejezes="", hozzaadas_kifejezes=""):
        self.dobas_kifejezes = dobas_kifejezes
        self.hozzaadas_kifejezes = hozzaadas_kifejezes

    def feldolgoz_dobas(self):
        """Külön kezeli a kockadobásokat, kiszámítja az eredményeket és visszaadja azokat."""
        minta = r'(\d*D\d+)'  # Kockadobások mintája, pl.: 2D8
        teljes_osszeg = 0
        eredmenyek = []

        for resz in re.findall(minta, self.dobas_kifejezes):
            darab, kocka_tipus = resz.split('D')
            darab = int(darab) if darab else 1
            kocka_tipus = int(kocka_tipus)

            # Kockadobás meghívása a `kocka` modulból
            dobas_eredmenyek, dobas_osszeg = kocka.dobas(kocka_tipus, darab)
            eredmenyek.append(f"{darab}D{kocka_tipus}: " + " | ".join(map(str, dobas_eredmenyek)))
            teljes_osszeg += dobas_osszeg

        return eredmenyek, teljes_osszeg

    def feldolgoz_hozzadas(self):
        """Külön kezeli a hozzáadott számokat és visszaadja az összegüket."""
        minta = r'([+-]?\s*\d+)'  # Számok keresése
        teljes_osszeg = 0

        for resz in re.findall(minta, self.hozzaadas_kifejezes):
            ertek = int(resz.replace(" ", ""))  # Whitespace eltávolítása
            teljes_osszeg += ertek

        return teljes_osszeg

    def osszesito_dobas_es_hozzadas(self):
        """Összesíti a kockadobások és módosítók eredményeit."""
        dobas_eredmenyek, dobas_osszeg = self.feldolgoz_dobas()
        hozzaadas_osszeg = self.feldolgoz_hozzadas()
        teljes_osszeg = dobas_osszeg + hozzaadas_osszeg
        return dobas_eredmenyek, hozzaadas_osszeg, teljes_osszeg


# GUI függvények
def szamitas():
    # Felhasználói bemenet beolvasása
    dobas_kifejezes = dobas_entry.get()  # Kockadobások
    hozzaadas_kifejezes = hozzaadas_entry.get()  # Módosítók

    # Kockadobo osztály példányosítása
    kockadobo = Kockadobo(dobas_kifejezes, hozzaadas_kifejezes)

    try:
        # Kifejezés feldolgozása
        dobas_eredmenyek, hozzaadas_osszeg, teljes_osszeg = kockadobo.osszesito_dobas_es_hozzadas()

        # Eredmények megjelenítése
        eredmenyek_label.config(text="Kockadobások:\n" + "\n".join(dobas_eredmenyek))
        modositok_label.config(text=f"Módosítók összesen: {hozzaadas_osszeg}")
        vegso_osszeg_label.config(text=f"Végső összeg: {teljes_osszeg}")

    except Exception as e:
        messagebox.showerror("Hiba", f"Hibás kifejezés! Kérlek próbáld újra.\nHiba: {str(e)}")


# Ablak inicializálása
root = tk.Tk()
root.title("RPG Kockadobó")
root.geometry("400x400")
root.minsize(400,400)

# Beviteli mezők
dobas_label = tk.Label(root, text="Add meg a kockadobásokat (pl. '1D6 + 2D8'):")
dobas_label.pack()

dobas_entry = tk.Entry(root, width=30)
dobas_entry.pack()

hozzaadas_label = tk.Label(root, text="Add meg a módosító számokat (pl. '+5 -3'):")
hozzaadas_label.pack()

hozzaadas_entry = tk.Entry(root, width=30)
hozzaadas_entry.pack()

# Eredmények megjelenítése
eredmenyek_label = tk.Label(root, text="Kockadobások:", justify=tk.LEFT)
eredmenyek_label.pack()

modositok_label = tk.Label(root, text="Módosítók összesen:", justify=tk.LEFT)
modositok_label.pack()

vegso_osszeg_label = tk.Label(root, text="Végső összeg: ", justify=tk.LEFT)
vegso_osszeg_label.pack()

# Gomb a számításhoz
szamitas_button = tk.Button(root, text="Számítás", command=szamitas)
szamitas_button.pack()

# Fő hurok
root.mainloop()