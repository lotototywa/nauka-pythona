# obicz średnią z listy

marks = [1, 5, 87, 45, 8, 8]
print (len (marks))

fika = 0
#print(fika)


# dla tymczasowej zmiennej ocena z listy marks
for ocena in marks:
    # krok1: fika == 0, ocena == 1
    # krok2: fika == 1, ocena == 5
    # krok3: fika == 6, ocena == 87
    fika = fika + ocena
srednia = fika / len (marks) 
okragla_srednia = int(srednia)
print (okragla_srednia)
