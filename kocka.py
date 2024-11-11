import random


def dobas(kocka_tipus, dobas_szam=1):

    eredmenyek = [random.randint(1, kocka_tipus) for _ in range(dobas_szam)]
    return eredmenyek, sum(eredmenyek)