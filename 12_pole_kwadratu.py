# napisz funkcję, która przyjmuje bok kwadratu jako argument i zwraca jego pole

def pole_kwadratu(bok):
    pole = bok * bok
    return pole
    
print (pole_kwadratu(12))

# napisz funkcję, która przyjmuje bok kwadratu jako argument i zwraca jego obwód
def obwud_kwadratu(bok):
    obwud = bok * 4
    return obwud
    
print (obwud_kwadratu(12))

# napisz funkcję, która przyjmuje obwód kwadratu jako argument i zwraca jego bok
def bok_z_obwodu(obwod):
    bok = obwod / 4
    return bok

print(bok_z_obwodu(48))

# napisz funkcję, która przyjmuje pole kwadratu jako argument i zwraca jego bok
import math
def bok_z_pola(pole):
    bok = math.sqrt(pole)

    return bok

print (bok_z_pola(144))