import random

print("----------------------------")
print("    ZGADNIJ NUMER - GRA")
print("----------------------------")
print()

numer = random.randint(1,5)

proba_tekst = input("zgadnij liczbę od 1 do 5: ")

proba = int (proba_tekst)
if numer==proba:
    print("brawo! udało ci się")
else:
    print(f"niestety chodziło o {numer}")


