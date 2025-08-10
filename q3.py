# "id": 3
# "titulo": "Encontrando o Segundo Maior Número"
# "descricao": "Crie uma função que retorne o segundo maior número de uma lista. Considere que a lista pode ter números duplicados."


def segundo_maior(lista):
    lista_unica = list(set(lista))  # remove duplicatas
    lista_unica.sort(reverse=True)
    return lista_unica[1] if len(lista_unica) > 1 else None

print(segundo_maior( numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]))
