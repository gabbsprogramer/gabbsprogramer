
def main():
    # print("oi")

    peso = float(input("digite seu peso: "))
    altura = float(input("digite sua altura em cm: "))

    imc = calcula_imc(peso, altura)
    print('seu imc é: {}'.format(round(imc, 2)))
    print('sua classificacao é: {}'.format(classificacao_corporal(imc)))

def calcula_imc(x, y):
    imc = x / (y/100) ** 2

    return imc

def classificacao_corporal(imc):
    if imc <= 18.5:
        return "magrez"
    elif imc <= 24.9 and imc > 18.5:
        return "normal"
    elif imc <= 29.9 and imc > 24.9:
        return "sobrepeso"
    elif imc <= 34.9 and imc > 29.9:
        return "obesidade I"
    elif imc <= 39.9 and imc > 34.9:
        return "obesidade II"
    else:
        return "obesidade III"





if __name__ == '__main__':
    main()
