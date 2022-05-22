#Soma, multiplicação e subtração em for/Summation, multiplication and subtraction in for

x = int(input('Insira um número: '))
soma = 0
multip = 1
subt = 0

for i in range(1, x+1):
    soma += i
    multip *= i
    subt -= i

print('Soma = {}, multiplicação {} e subtração {}'.format(soma, multip, subt))
