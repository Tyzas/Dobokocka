import random


def dobas(kocka_tipus, dobas_szam=1):
    """
    Kockadobás szimulátor. Megadott oldalú kockát dob a megadott alkalommal.

    :param kocka_tipus: Kocka oldalainak száma (pl. 6 a D6-hoz, 20 a D20-hoz)
    :param dobas_szam: Hányszor dobjon a kockával
    :return: Lista a dobások eredményeiről és az összegük
    """
    eredmenyek = [random.randint(1, kocka_tipus) for _ in range(dobas_szam)]
    return eredmenyek, sum(eredmenyek)