# "id": 14,
# "titulo": "Calculando a Média"
# "descricao": "Crie uma função que receba uma lista de números e retorne a média aritmética desses valores."

def soma_recursiva(lista):
    if not lista:
        return 0
    return lista[0] + soma_recursiva(lista[1:])

def contar_recursivo(lista):
    if not lista:
        return 0
    return 1 + contar_recursivo(lista[1:])

def calcular_media(lista):
    if not lista:
        return 0
    soma = soma_recursiva(lista)
    quantidade = contar_recursivo(lista)
    return soma / quantidade

numeros = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3, 42, 999999, 5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]

print("Média:", calcular_media(numeros))
