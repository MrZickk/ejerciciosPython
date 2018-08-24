
def bubblesort(lista):
    bandera=0
    for i in range(len(lista)):
        while bandera < 4:
            for j in range(len(lista)-1):
                if lista[j] > lista[j +1]:
                    lista[j], lista[j +1] = lista[j +1], lista[j]
                else:
                    bandera = bandera+1
        break

lista=[8, 3, 7, -5, 1]
bubblesort(lista)
print(lista)
