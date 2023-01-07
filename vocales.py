vocales = ['a', 'e', 'i', 'o', 'u']
palabras = 'Perfectamente  bien para todos?'
lista_vacia = []
for p in palabras:
    if p in vocales:
        if p not in lista_vacia:
            lista_vacia.append(p)
for l in lista_vacia:
    print(l)
