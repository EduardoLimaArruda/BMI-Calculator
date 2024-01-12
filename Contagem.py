altura = input()
peso = input()
altura_int = float(altura)
peso_int = int(peso)

IMC = peso_int / (altura_int ** 2)

print(type(altura))
print(type(peso))

print(IMC)


