#    "id": 9,
#    "titulo": "Contando Ocorrências",
#    "descricao": "Desenvolva uma função que receba uma lista e um valor. A função deve contar quantas vezes esse valor aparece na lista e retornar o total

def contar_ocorrencias(lista, valor):
    return len(list(filter(lambda x: x == valor, lista)))


numeros = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3, 42, 999999, 5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]

print("Quantas vezes o número 2 aparece?", contar_ocorrencias(numeros, 2))
print("Quantas vezes o número 13 aparece?", contar_ocorrencias(numeros, 13))
print("Quantas vezes o número 999 aparece?", contar_ocorrencias(numeros, 999))
