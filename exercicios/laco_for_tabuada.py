tabuada=int(input("Informe a tabuada: "))
print("Tabuada do némuro", tabuada)
for valor in range(1,11,1):
    print(str(tabuada) + " x " + str(valor) + " = " + str((tabuada*valor)))