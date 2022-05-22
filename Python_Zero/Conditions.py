#Programa voltado a ensinar a utilizar as condicionais If, Elif e Else

x = int(input('Insira um valor para a variável x: / Enter a value for the variable x: '))

y = int(input('Insira um valor para a variável y: / Enter a value for the variable y: '))

if x > y:
    print('A variável {} é maior que a variável {}'.format(x,y))

elif y > x:
    print('A variável {} é maior que a variável {}'.format(y,x))

else:
    print('A variável {} é igual a variável {}'.format(x,y))

