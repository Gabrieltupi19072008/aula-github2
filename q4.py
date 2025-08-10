#"id": 4,
#    "titulo": "Encontrando os Números Pares",
#    "descricao": "Desenvolva uma função que receba uma lista de números inteiros e retorne uma nova lista contendo apenas os números pares."


def numeros_pares(lista):
    return [n for n in lista if n % 2 == 0]

print(numeros_pares( numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]))

