import random
''' Tutaj Jacek opisze na czym polega ten program i jak on działa.'''
# Najpierw otwieramy tekst z wyrazami
f = open("diceware-pl.txt", "r")
# Tworzymy listę Lines
lines = f.readlines() 
# Potem tworzymy string Hasło
haslo = ""
# Robimy pętlę powtarzającą się 5 razy
for i in range(5):
    # Następnie losujemy jeden wyraz z 7776 wyrazów
    wynik = random.choice(lines) 
    # Później wyciągamy wyraz z linijki
    wynik = wynik.split(' ')[1]
    # Potem powiększamy pierwszą literę
    wynik = wynik.capitalize()
    # Następnie do hasła dodajemy wynik z usuniętymi spacjami 
    # i enterami (przed i po)
    haslo = haslo + wynik.strip()

# I na koniec "drukujemy" :-)
print(haslo)