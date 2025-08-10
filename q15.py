#"id": 15,
#"titulo": "Invertendo a Lista",
#"descricao": "Escreva uma função que receba uma lista e retorne uma nova lista com os elementos na ordem inversa."

def inverter_lista(lista):
    invertida = []
    for i in range(len(lista)-1, -1, -1):
        invertida.append(lista[i])
    return invertida

numeros = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3, 42, 999999, 5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]

print("Lista original:", numeros)
print("Lista invertida:", inverter_lista(numeros))
