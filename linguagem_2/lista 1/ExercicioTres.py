"""Crie uma classe calculadora com as quatro operações básicas (soma, subtração, multiplicação e divisão). 
O usuário deve informar dois números e o programa deve fazer as quatro operações. (modifique para calcular tudo no mesmo método, 
somando 1 ao resultado de cada operação)"""

class Calculadora:
    def calcular_soma(self, numero1, numero2):
        soma = numero1 + numero2
        print("A soma é:", soma)

    def calcular_subtracao(self, numero1, numero2):
        subtracao = numero1 - numero2
        print("A Subtracao é:", subtracao)

    def calcular_multiplicacao(self, numero1, numero2):
        multiplicacao = numero2 * numero1
        print("A Multiplicacao é:", multiplicacao)

    def calcular_divisao(self, numero1, numero2):
        divisao = numero2 / numero1
        print("A Divisao é:", divisao)


calcular = Calculadora()

print('Digite o número 1')
numero1 = int(input())

print('Digite o número 2')
numero2 = int(input())

calcular.calcular_soma(numero1, numero2)
calcular.calcular_subtracao(numero1, numero2)
calcular.calcular_multiplicacao(numero1, numero2)
calcular.calcular_divisao(numero1, numero2)