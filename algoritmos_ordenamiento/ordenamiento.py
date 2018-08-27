
def bubblesort(lista):
    bandera=1
    for i in range(len(lista)):
        if bandera > 0:
            for j in range(len(lista)-1):
                if lista[j] > lista[j +1]:
                    lista[j], lista[j +1] = lista[j +1], lista[j]
                    bandera += 1


