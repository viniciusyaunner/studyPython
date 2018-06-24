dia = float(input("Por favor, entre com o número de dias que deseja converter: "))
hor = float(input("Por favor, entre com o número de horas que deseja converter: "))
min = float(input("Por favor, entre com o número de minutos que deseja converter: "))
seg = float(input("Por favor, entre com o número de srgundos que deseja converter: "))

minu = min * 60
hora = hor * 3600
dias = dia * 24
dias = dias * 3600



print ("o total em segundos é:", float(minu+hora+dias+seg),"segundos")
