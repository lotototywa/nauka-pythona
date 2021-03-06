def solution(a, b):
    if len(a) > len(b):
        return b + a+ b
    else:
        return a + b + a 

BASIC_TESTS = (
    (('45', '1'), '1451'),
    (('13', '200'), '1320013'),
    (('Soon', 'Me'), 'MeSoonMe'),
    (('U', 'False'), 'UFalseU')
)

for pair, result in BASIC_TESTS:
    assert solution(*pair) == result
