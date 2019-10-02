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