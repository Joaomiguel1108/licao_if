angulo1 = int(input("Digite um ângulo do triângulo"))
angulo2 = int(input("Digite outro ângulo do triângulo"))
angulo3 = int(input("Digite mais um ângulo do triângulo"))

if angulo3 == 90 or angulo2 ==90 or angulo1 == 90:
    print("triângulo retangulo ")
elif angulo3 > 90 or angulo2 > 90 or angulo1 > 90:
    print("triângulo Obtusângulo ")
elif angulo3 < 90 and angulo2 < 90 and angulo1 < 90:
    print("triângulo Acutângulo ")
