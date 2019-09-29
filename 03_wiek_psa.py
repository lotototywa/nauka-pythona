# spytaj uzytkownika o imie psa
# spytaj uzytkownika o wiek psa
# przemnóz wiek psa przez 7, aby uzyskać wiek psa w ludzkich latach
# zwroc uzytkownikowi wynik:
"""
Twoj pies {imie_psa} 
mialby jako czlowiek {wiek_w_ludzkich_latach} lat(a)
"""

# spytaj uzytkownika o imie psa
imie_psa = input("Jak na imię ma twój pies? ")

# spytaj uzytkownika o wiek psa
wiek_psa = input("ile lat ma twoj pies? ")

# napisz podsumowanie

print(f"Twoj pies {imie_psa} ma {wiek_psa} lat/a")



ludzki_wiek = int(wiek_psa) * 7
print(f" jako czlowiek twoj pies mialby {ludzki_wiek} lat/a")