
def div_list(lista):
    if len(lista) == 1 or len(lista) == 0:
        return lista
    
    mitad=(len(lista))//2
    izquierda=div_list(lista[:mitad])
    derecha=div_list(lista[mitad:])

    lista_tmp=[]
    i=0
    j=0
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            print(i)
            print(izquierda[i], derecha[j], 'i,j')
            lista_tmp.append(izquierda[i])
            print(lista_tmp, 'tmp')
            i += 1
            print(i)
        else:
            lista_tmp.append(derecha[j])
            j += 1
            print(j, 'j')
            print(lista_tmp, 'tmp2')
    lista_tmp += derecha[j:]
    print(lista_tmp, 'derecha')
    lista_tmp += izquierda[i:]
    print(lista_tmp, 'izquierda')

    return lista_tmp


lista=[7, 3, 4, -5, 1]
div_list(lista)
