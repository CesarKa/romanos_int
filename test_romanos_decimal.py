import romanos_int

def traducir_romano():

    assert romanos_int("") == 0
    assert romanos_int(" ") == 0
    assert romanos_int("I") == 1
    assert romanos_int("III") == 3
    assert romanos_int("IV") == 4
    assert romanos_int("IX") == 9
    assert romanos_int("X") == 10

def traducir_romano():

    assert romanos_int("XXIX") == 29
    assert romanos_int("LVIII") == 58
    assert romanos_int("XL") == 40
    assert romanos_int("XC") == 90
    assert romanos_int("CD") == 400
    assert romanos_int("CM") == 900

def traducir_romano():

    assert romanos_int("M") == 1000
    assert romanos_int("MCMLV") == 1955
    assert romanos_int("MCMLXXXVII") == 1987
    assert romanos_int("MMMCMXCIX") ==  3999
    assert romanos_int("MCMXCIV") == 1994
    assert romanos_int("MMXXIII") == 2023
    assert romanos_int("MMMM") == 4000