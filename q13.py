#     "id": 13,
#    "titulo": "Retornando o Menor Número",
#    "descricao": "Desenvolva uma função que receba uma lista de números e retorne o menor número encontrado nela."

def encontrar_menor(lista):
    menor = lista[0]
    i = 1
    while i < len(lista):
        if lista[i] < menor:
            menor = lista[i]
        i += 1
    return menor

numeros = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3, 42, 999999, 5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]

print("Menor número:", encontrar_menor(numeros))
