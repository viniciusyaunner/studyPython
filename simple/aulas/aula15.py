"""
n funciona
lista_num = [100,200,300,400]
for item in lista_num:
    item += 1000
print(lista_num)
"""

"""
funciona
lista_num = [100,200,300,400,500,600,700]
for item in range(len(lista_num)):
    lista_num[item] += 1000
print(lista_num)
"""

lista_num = [100,200,300,400,500,600,700]
for item in enumerate(lista_num):
    lista_num[item] += 1000
print(lista_num)