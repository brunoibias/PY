""" Autor: Bruno Ibias
Este código calcula o IMC(índice de massa corporal) e mostra em q categoria esta
tambem calcula a media de idade de e a media de IMC do total"""


mediaIdade = 0
mediaIMC = 0
repeticao = 0

#este laço conta e informa o IMC
while (True):
    idade = int(input('Digite a sua idade  '))
    if (idade == 0):
        break
    valorDoPeso = float(input('Digite seu peso '))
    valorAltura = float(input('Digite sua altura '))
    formula = valorDoPeso / (valorAltura * valorAltura)
    formatarFormula = round(formula, 2)
    if (formatarFormula < 16.00):
        print('Seu IMC é:',formatarFormula,'Você esta com Baixo peso Grau III')
    elif (formatarFormula > 16.01) and (formatarFormula < 16.99):
        print('Seu IMC é:',formatarFormula,'Você esta com Baixo peso Grau II')
    elif (formatarFormula > 17.01) and (formatarFormula < 18.49):
        print('Seu IMC é:',formatarFormula,'Você esta com Baixo peso Grau I')
    elif (formatarFormula > 18.50) and (formatarFormula < 24.99):
        print('Seu IMC é:',formatarFormula,'Você esta no Peso Ideal')
    elif (formatarFormula > 25.00) and (formatarFormula < 29.99):
        print('Seu IMC é:',formatarFormula,'Você esta com Sobrepeso')
    elif (formatarFormula > 30.00) and (formatarFormula < 34.99):
        print('Seu IMC é:',formatarFormula,'Você esta com Obesidade Grau I')
    elif (formatarFormula > 35.00) and (formatarFormula < 39.99):
        print('Seu IMC é:',formatarFormula,'Você esta com Obesidade Grau II')
    else:
        print('Seu IMC é:',formatarFormula,'Você esta com Obesidade Grau III')
#estes sao os contadores
    repeticao += 1
    mediaIdade = ((mediaIdade + idade) / repeticao)
mediaIMC = ((mediaIMC + formatarFormula) / repeticao)

print('A media do IMC', mediaIMC)
print('A media da Idade', mediaIdade)

# esta condiçao mostra o IMC da media
if (mediaIMC < 16.00):
    print('A media é Baixo peso Grau III')
elif (mediaIMC > 16.01) and (mediaIMC < 16.99):
    print('A media é  Baixo peso Grau II')
elif (mediaIMC > 17.01) and (mediaIMC < 18.49):
    print('A media é Baixo peso Grau I')
elif (mediaIMC > 18.50) and (mediaIMC < 24.99):
    print('A media é Peso Ideal')
elif (mediaIMC > 25.00) and (mediaIMC < 29.99):
    print('A media é Sobrepeso')
elif (mediaIMC > 30.00) and (mediaIMC < 34.99):
    print('A media é Obesidade Grau I')
elif (mediaIMC > 35.00) and (mediaIMC < 39.99):
    print('A media é Obesidade Grau II')
else:
    print('A media é Obesidade Grau III')


print('__________________Fim do Programa !__________________')
