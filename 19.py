altura = float(input("Digite sua altura"))
sexo = str(input("Voçê é homem ou mulher?"))

if sexo == 'homem':
    print((72.7 * altura)-58)
elif sexo == 'mulher':
    print((62.1 * altura)-44.7)
