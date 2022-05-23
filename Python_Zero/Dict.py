cardapio = {'Lanche' : 10.9, 'Batata' : 5.5, 'Refrigerante' : 3.9}

print('-'*40)
print('-'*15,'CARDAPIO','-'*15)
print('-'*40)

for k, v in cardapio.items():

    print(f'{k:.<20} R${v:5.2f}')

print('-'*40)

qtd_cliente = {}

for k in cardapio.keys():

    qtd_cliente [k] = int(input(f'Quantos {k} você quer? '))

print('-'*40)

#print(qtd_cliente)

soma = 0

for v1, v2 in zip(cardapio.values(), qtd_cliente.values()):

    soma += v1 * v2

print(f"O valor total da conta é de R${soma:.2f}")


print('-'*40)
print('-'*11, 'RECIBO', '-'*11)

for k, v in qtd_cliente.items():
    print(f"{v} {k:.<20} R${v * cardapio[k]:5.2f}")

print('-'*30)
print(f'Total R$ {soma:.2f}')
