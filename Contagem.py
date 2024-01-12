print("BMI Calculator")
altura = input("Qual a sua altura?\n")
peso = input("Qual o seu peso?\n")
altura_int = float(altura)
peso_int = int(peso)

IMC = peso_int / (altura_int ** 2)
print("\nSeu IMC é " + str(IMC))

enter = input("\n\nAperte Enter para fechar")
