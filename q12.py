#"id": 12,
#    "titulo": "Juntando Duas Listas",
#    "descricao": "Crie uma função que receba duas listas e retorne uma terceira lista que seja a concatenação das duas."

def recebe_duas(lista1, lista2):
    lista3 = []
    for item in lista1:
        lista3.append(item)
    for item in lista2:
        lista3.append(item)
    return lista3

natureza = ["rio", "floresta", "leão", "montanha", "oceano", "estrela", "vento", "cachoeira", "lua", "girassol"]
tecnologia = ["algoritmo", "API", "blockchain", "código", "software", "nuvem", "hardware", "interface", "pixel", "servidor"]

print("A lista concatenada fica:", recebe_duas(natureza, tecnologia))
