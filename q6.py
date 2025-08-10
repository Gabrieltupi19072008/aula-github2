#"id": 6,
#    "titulo": "Buscando um Número",
#   "descricao": "Elabore uma função que receba um número e uma lista. A função deve buscar o número na lista e retornar 'True' se o encontrar e 'False' caso contrário."

def buscar_numero(numero, lista):
    for elemento in lista:
        if elemento == numero:
            return True
    return False


numeros = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3, 42, 999999, 5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]

print("Número 5 está na lista?", buscar_numero(5, numeros))
print("Número 77 está na lista?", buscar_numero(77, numeros))
