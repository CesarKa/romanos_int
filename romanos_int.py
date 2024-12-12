

def romanos_int(signo):


    valor_romanos = { 
        "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000 
    }
    return valor_romanos.get(signo, 0)


def traducir_romano(expresion):

    total = 0
    n_previo = 0
    for signo in expresion:
        valor = romanos_int(signo)
        if n_previo >= valor:
            total += valor
        else:
            total += valor - 2 * n_previo 
        n_previo = valor

    return total
    

expresion = input("Expresion romana que traducir: ")


numero_traducido = traducir_romano(expresion) 
print(f"Número traducido: {numero_traducido}")





