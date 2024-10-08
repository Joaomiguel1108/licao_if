peso = int(input("digite seu peso"))

altura = float(input("digite a sua altura"))

imc = (peso / (altura * altura))

print(f"seu IMC é {imc}")

if imc <20:
    print("abaixo do normal")
elif imc <=20 and imc >=25:
    print("normal")
elif imc <=25 and imc >=30:
    print("sobrepeso")
elif imc <=30 and imc >=35:
    print("obesidade leve")
elif imc <=35 and imc >=40:
    print("obesidade moderada")
elif imc >40:
    print("obesidade morbida")
