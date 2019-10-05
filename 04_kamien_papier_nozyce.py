"""
Tu Lotototata. Podłączyłem się w VS Code przez Live Session do edytora Jacka.

Teraz chcemy zrobić kolejny etap.

Ostatnim razem zrobiliśmy listę przedmiotów i zapisywaliśmy od gracza jego wybór. 

Teraz chcemy wylosować za komputer i porównać odpowiedzi.

1. Losowanie (i wyświetlenie co komputer wybrał)
2. Porównanie odpowiedzi i wyświetlenie wyniku
"""

import random

przedmioty = ["kamień", "papier", "nożyce"]

wybor_gracza = input(
    "wybierz "
    + ", ".join(
        [
            "kamień", 
            "papier", 
            "nożyce"
        ])
    + ": "
    )

print (f"wybrałeś {wybor_gracza}")

# 1. Losowanie i zapisanie wyniku losowania do zmiennej wybor_komputera
wybor_komputera = random.choice(przedmioty)

# 1b. wyświetlenie co komputer wybrał, np. Wybór komputera:" ____"
print(f'Wybór komputera: {wybor_komputera}')

# 2. Porównanie odpowiedzi