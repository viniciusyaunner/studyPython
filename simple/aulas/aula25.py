lista = [11,10,12]
tupla = 11,10,12
def func(a,b,c):
    print(a)
    print(b)
    print(c)

"""lista.sort()
func(*lista)
"""
l = [*tupla]
l.sort()
func(*l)