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

# 2. Porównanie odpowiedzi (sposób najprostszy i najbrzydszy)

if wybor_gracza == wybor_komputera:
    print(f'REMIS, gracz i komuter wybrali {wybor_gracza}')
elif wybor_gracza == 'kamień' and wybor_komputera == 'papier':
    print(f'Wygrywa KOMPUTER! Papier owija kamień.')
elif wybor_gracza == 'papier' and wybor_komputera == 'nożyce':
    print(f'Wygrywa KOMPUTER! Nożyce tną papier.')
elif wybor_gracza == 'nożyce' and wybor_komputera == 'kamień':
    print(f'Wygrywa KOMPUTER! kamień tępi nożyce.')
elif wybor_gracza == 'kamień' and wybor_komputera == 'nożyce':
    print(f'Wygrywa GRACZ! kamień tępi nożyce')
elif wybor_gracza == 'nożyce' and wybor_komputera == 'papier':
    print(f'Wygrywa GRACZ! Nożyce tną papier ')
elif wybor_gracza == 'papier' and wybor_komputera == 'kamień':
    print(f'Wygrywa GRACZ! Papier owija kamień.')
else:
    print('Wystąpił nieoczekiwany błąd. Może podałeś nieprawidłowy przedmiot?')


"""
(tu znowu lotototata, komentuję przez VS Code Live Share)

Na tym etapie gra jest gotowa, ale kod i rozgrywkę możemy usprawnić.
Przykłady:
  * Obsługa przypadku kiedy gracz poda nieprawidłową wartość i zapytanie ponownie
  * Może zamiast podawać pełny przedmiot, wystarczy pierwsza litera? Np. k zamiast kamień?
  * Może też program powinien akceptować przedmioty bez polskich liter i o dowolnej wielkości znaków?
  * Może ta gra nie powinna się kończyć za pierwszym razem tylko koleje losowanie i wyświetlanie wyników?
  * Może gra powinna przyjmować parametry, np. do imię gracza albo do ilu punktów gramy?
  * Może wprowadzimy kolory do konsoli, żeby łatwiej się rozpoznawało kto wygrał, co wybrał, etc?
"""