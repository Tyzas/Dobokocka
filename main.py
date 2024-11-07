import tkinter as tk
from kocka import dobas  # Importáljuk a saját kocka modult


def dobas_esemeny():
    """Eseménykezelő a kockadobás gombhoz."""
    try:
        kocka_tipus = int(kocka_tipus_entry.get())
        dobas_szam = int(dobas_szam_entry.get())
        eredmenyek, osszeg = dobas(kocka_tipus, dobas_szam)

        # Dobásonkénti eredmények formázása megjelenítéshez
        eredmeny_text = " | ".join(str(eredmeny) for eredmeny in eredmenyek)
        eredmeny_label.config(text=f"Eredmények: {eredmeny_text}\nÖsszeg: {osszeg}")
    except ValueError:
        eredmeny_label.config(text="Hiba: Kérlek, számokat adj meg!")


# Létrehozzuk a fő ablakot
root = tk.Tk()
root.title("Kockadobás Szimulátor")

# Feliratok és beviteli mezők
tk.Label(root, text="Kocka oldalainak száma (pl. 6 a D6-hoz):").pack()
kocka_tipus_entry = tk.Entry(root)
kocka_tipus_entry.pack()

tk.Label(root, text="Hányszor dobjunk?").pack()
dobas_szam_entry = tk.Entry(root)
dobas_szam_entry.pack()

# Dobás gomb
dobas_gomb = tk.Button(root, text="Dobás", command=dobas_esemeny)
dobas_gomb.pack()

# Eredmény megjelenítése
eredmeny_label = tk.Label(root, text="Eredmények itt jelennek meg")
eredmeny_label.pack()

# Fő eseményciklus elindítása
root.mainloop()