"""" operadores logicos
2<4 and 2==4
2>4 or 2<4
not (2>4 or 2<4)
2 is 2
type(2)
type (2.0) is int
"""
n1 = int(input("digite um numero: "))
if(n1>10):
    print("o valor é maior  que 10")
    if(n1<=15):
        print("o valor é igual ou menor que 15")
    else:
        if(n1<=50):
            print("o valor é menor ou igual a 50")
        else:
            print("o valor é maior que 50")
else:
    if(n1>5):
        print(" numero é maior que 5")
        if(n1==7):
            print("o numero é maior que 7")
    else:
        print("o valor é menor do que 5")
