lista = [1, 2, 3, 3, 3, 3, 4, 5]
newlist = []


def func(lista, newlist):
    for cont in lista:
        if (cont not in newlist):
            newlist.append(cont)

    print(newlist)
func(lista,newlist)