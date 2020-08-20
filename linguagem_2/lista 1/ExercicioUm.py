"""receba 5 alunos, 3 notas para cada um e 
calcule a média mostrando se está aprovado ou não"""

class Calculadora:

contacasado = 0
contasolteiro = 0
contaseparado =0
contaviuvo = 0

#este laço pede a idade e se ela for igual a ZERO o programa para
while (True):
    idade = int(input('Digite a sua idade, digite 0(zero) para sair: '))
    if idade == 0:
        break
    
     #esta linha pede o estado civil
    CIVIL = (input('Digite seu estado civil\n 1 para casado(a)\n 2 para solteiro(a)\n 3 para viuvo(a)\n 4 para separado(a)'))
    if (CIVIL == '1'):
        contacasado+=1
    elif (CIVIL == '2'):
        contasolteiro+=1
    elif (CIVIL == '3'):
        contaviuvo+=1
    elif (CIVIL == '4'):
        contaseparado+=1
    elif (CIVIL == '666'):
            print ('AVE SATÃN')
    else:print('O que você digitou não é válido, repita processo')


print('O total de casados é:',contacasado)
print('O total de solteiros é:',contasolteiro)
print('O total de viuvos é:',contaviuvo)
print('O total de separados é:',contaseparado)