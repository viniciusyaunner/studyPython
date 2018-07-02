# try:
#     a = 10 / 0
#     print(a)
# except ZeroDivisionError:
#     print("n é possivel dividir por 0")

def input_float(msg):
    while True:
        try:
            return float(input(msg))
        except ValueError:
            print("o numero é invalido")


n1 = input_float("digite um numero: ")
n2 = input_float("digite outro numero: ")

try:
    print(n1/n2)
except ZeroDivisionError:
    print("Não é possivel dividir por zero")