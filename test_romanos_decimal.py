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

def test_validad_caracteres_romanos():
    with pytest.raises(RomanNumberError) as contexto:
        romanos_a_enteros("ZTW")
    assert str(contexto.value).endswith("no es un simbolo romano")

def test_validar_no_repeticiones_de_mas_de_1():
    """
    I, X, C, M hasta 3 veces
    """
    assert valida_repeticiones('IIII') == (False, "I", 4)
    assert valida_repeticiones("XXXX") == (False, "X", 4)
    assert valida_repeticiones("CCCC") == (False, "C", 4)
    assert valida_repeticiones("MMMM") == (False, "M", 4)


def test_validar_repeticiones_no_mas_de_3():
    """
    V, L, D no se pueden repetir
    """
    assert valida_repeticiones("VV") == (False, "V", 2)
    assert valida_repeticiones("DD") == (False, "D", 2)
    assert valida_repeticiones("LL") == (False, "L", 2)


def test_validar_romano_cuatro_repeticiones():
    with pytest.raises(RomanNumberError) as contexto:
        romanos_a_enteros("MCCCCXXII")
    assert str(contexto.value) == "C solo puede repetirse tres veces"


def test_validar_romano_cuatro_repeticiones():
    with pytest.raises(RomanNumberError) as contexto:
        romanos_a_enteros("MCCVV")
    assert str(contexto.value) == "V no puede repetirse"

def test_restas_incorrectas():
    with pytest.raises(RomanNumberError):
        romanos_a_enteros("IC")

    with pytest.raises(RomanNumberError):
        romanos_a_enteros("VX")