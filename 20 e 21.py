lados = int(input("Digite o numero de lados"))
tamanho = float(input("Digite o tamanho dos lados"))

if lados == 3:
    print("TRIÂNGULO, com area de", tamanho*lados)
elif lados == 4:
    print("QUADRADO, com area de", tamanho*lados)
elif lados == 5:
    print("PENTÁGONO, com area de", tamanho*lados)
elif lados<3:
    print("Não é um polígono")
elif lados>5:
    print("POLÍGONO NÃO IDENTIFICADO.")
