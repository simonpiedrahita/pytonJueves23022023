# Condicionales en python 
nivelDeAgua = int(input("digital el nivel del agua "))
#while nivelDeAgua != 0:
if nivelDeAgua >=0 and nivelDeAgua<=250:
    print(f'el nivel de agua es muy bajo {nivelDeAgua}U')
elif nivelDeAgua >250 and nivelDeAgua <=450:
    print(f'el nivel de agua es optimo {nivelDeAgua}U')
elif nivelDeAgua < 450 :
    print(f'el nivel de agua es Critico!, EVACUE {nivelDeAgua}U')
else:
    print('revise el sensor')
#print("gracias ")