""" Given a string of digits, you should replace any digit below 5 with '0' 
and any digit 5 and above with '1'. Return the resulting string.

https://www.codewars.com/kata/57eae65a4321032ce000002d/train/python
"""

def fake_bin(x):
    nowa = ""
    for coś in x:
        coś = int(coś)
        if coś < 5:
            nowa += "0"
        else:
            nowa += "1"
    return nowa

rezultat = fake_bin("29834723947234987")
print(rezultat)