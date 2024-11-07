import tkinter as tk
from tkinter import filedialog, messagebox
from kocka import dobas

# Dobási eredmény lista
dobasok_tortenete = []


def dobas_esemeny():
    """Eseménykezelő a kockadobás gombhoz."""
    try:
        kocka_tipus = int(kocka_tipus_entry.get())
        dobas_szam = int(dobas_szam_entry.get())
        eredmenyek, osszeg = dobas(kocka_tipus, dobas_szam)

        # Dobásonkénti eredmények formázása megjelenítéshez
        eredmeny_text = " | ".join(str(eredmeny) for eredmeny in eredmenyek)

        # Eredmény mentése a történetbe
        dobasi_eredmeny = f"Kocka: D{kocka_tipus}, Dobások száma: {dobas_szam}, Eredmények: {eredmeny_text}, Összeg: {osszeg}"
        dobasok_tortenete.append(dobasi_eredmeny)

        # Eredmény kiíratása
        eredmeny_label.config(text=dobasi_eredmeny)
    except ValueError:
        eredmeny_label.config(text="Hiba: Kérlek, számokat adj meg!")


def mentes():
    """Dobási történet mentése fájlba."""
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Szöveg fájlok", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            for sor in dobasok_tortenete:
                file.write(sor + "\n")
        messagebox.showinfo("Mentés", "A dobások sikeresen elmentve!")


def betoltes():
    """Dobási történet betöltése fájlból."""
    file_path = filedialog.askopenfilename(filetypes=[("Szöveg fájlok", "*.txt")])
    if file_path:
        with open(file_path, "r") as file:
            betoltott_tortenet = file.readlines()

        # Betöltött történet kiíratása
        dobasi_szoveg = "".join(betoltott_tortenet)
        eredmeny_label.config(text=f"Betöltött történet:\n{dobasi_szoveg}")

        # Betöltött történet mentése a dobások történetébe (ha folytatni szeretnénk)
        dobasok_tortenete.extend([sor.strip() for sor in betoltott_tortenet])


# fő ablak
root = tk.Tk()
root.title("Kockadobás Szimulátor")
root.geometry("600x400")
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

# Mentés és betöltés gombok
mentes_gomb = tk.Button(root, text="Mentés", command=mentes)
mentes_gomb.pack()

betoltes_gomb = tk.Button(root, text="Betöltés", command=betoltes)
betoltes_gomb.pack()

# Fő eseményciklus elindítása
root.mainloop()