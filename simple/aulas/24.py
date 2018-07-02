"""def lista_de_argumento(*lista):
    print(lista)

def lista_de_argumentos_assossiativos(**dicionario):
    print(dicionario)

lista_de_argumento(1,2,3,4,5,6)
lista_de_argumento("um","dois","tres")

lista_de_argumentos_assossiativos(a=1,b=2,c=3)
lista_de_argumentos_assossiativos(um=1,dois=2,tres=3,quatro=4)
"""
def pessoa(nome,sobrenome,idade):
    print(nome)
    print(sobrenome)
    print(idade)

"""lista = "scrpt","asda",14
#pessoa(tupla[0], tupla[1], tupla[2])
pessoa(*lista)
"""
d = {"nome":"script","sobrenome":"ads","idade":13}
pessoa(**d)