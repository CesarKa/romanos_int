

def romanos_int(signo):


    valor_romanos = { 
        "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000 
    }
    return valor_romanos.get(signo, 0)


def traducir_romano(expresion):
    valida, char = valida_repeticiones(expresion)
    if not valida:    
        raise ValueError(f"{char}Solo puede repetirse tres veces")

    total = 0
    n_previo = 0
    for signo in expresion:
        valor = romanos_int(signo)
        if valor == 0:
            raise ValueError(f"Caracter inválido: {signo}")
        if n_previo >= valor:
            total += valor
        else:
            total += valor - 2 * n_previo 
        n_previo = valor

    return total
    

def esta_en_racha(expresion,signo:str,racha:int)->bool:
    cont = 0
    if len(expresion) >= racha:
        for el in expresion:
            if el == signo:
                cont += 1
                if cont == racha:
                    break
            else:
                cont = 0
    else:
        cont = 0
    return cont == racha

def valida_repeticiones(num_roman):
    not_repeat = [("I", 4), ("X", 4), ("V", 2), ("D", 2), ("L", 2)
                  ("M", 4), ("C", 4)]
    result = True

    for char in not_repeat:
        if esta_en_racha(num_roman, char, 4):
            result = False
            break
    return result, char





expresion = input("Expresion romana que traducir: ")
numero_traducido = traducir_romano(expresion) 
print(f"Número traducido: {numero_traducido}")





