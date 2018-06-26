"""a = 10
b = 25
c = 66

x = int(input("digite um numero: "))

#if(x == a or x == b or x == c):
#if(x in [10,25,66]):
if (x in [a, b, c]):
    print("esta cotido")
else:
    print("não esta contido")
"""

cores = ["azul","amarelo","vermelho","branca"]

while True:
    cor = input("Digite o nome de uma cor ou 0 pra parar: ")
    if(cor=="0"):
        break
    elif cor in cores:
        print("essa cor esta contida")
    else:
        print("essa cor não esta contida")
print()
