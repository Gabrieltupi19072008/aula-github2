#   "id": 8,
#    "titulo": "Somando os Valores da Lista",
#    "descricao": "Crie uma função que receba uma lista de números e retorne a soma de todos os seus valores."

def somar_valores(lista):
    if not lista:  # Caso base: lista vazia
        return 0
    return lista[0] + somar_valores(lista[1:])  # soma o primeiro com o resto


numeros = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3, 42, 999999, 5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]

print("Soma dos valores:", somar_valores(numeros))
