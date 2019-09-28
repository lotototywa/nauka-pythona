# random to biblioteka którą trzeba importować, 
# niektóre biblioteki są w pakiecie pythona ale niektóre nie, a random jest
# więc by importować random trzeba napisać import random 
import random

lista_imion = ["jacek","jagoda","dominik","kasia"]
moje_imie=random.choice(lista_imion)
print(f'Cześć, jestem {moje_imie}!')
