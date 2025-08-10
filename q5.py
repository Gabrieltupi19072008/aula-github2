#    "id": 5,
#    "titulo": "Encontrando os Números Ímpares",
#   "descricao": "Crie uma função que filtre uma lista de números e retorne apenas os números ímpares."


def numeros_impares(lista):
    return [n for n in lista if n % 2 != 0]

print(numeros_impares( numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]))
