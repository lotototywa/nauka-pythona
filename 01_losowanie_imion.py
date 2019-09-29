"""
    Cześć, tu Korsnislaw, lub Lotototata, czyli tata Lotototywy.
    Pokazuję właśnie synowi, do czego służy GitHub i jak go używać.

    W tej chwili mam sklonowane repozytorium i będę chciał zrobić pull requesta.
    Pull request oznacza, że chcę żeby moje zmiany w programie były 
    przyjęte do kodu właściela repozytorium, czyli przez Lotototywę.

    No to spróbujmy teraz zapisać ten plik, zrobić commit i pull request.
"""

# random to biblioteka którą trzeba importować, 
# niektóre biblioteki są w pakiecie pythona ale niektóre nie, a random jest
# więc by importować random trzeba napisać import random 
import random

# to jest zmienna do której przypisuje liste imion z mojej rodziny
lista_imion = ["jacek","jagoda","dominik","kasia"]

# funkcja random.choice wybiera losowy element z podanej listy 
moje_imie = random.choice(lista_imion)

# a teraz wyświetla mi się wylosowany element na ekranie
print(f'Cześć, jestem {moje_imie}!')
