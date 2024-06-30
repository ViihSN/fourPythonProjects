
print('Bem-vindos à loja de Marmitas da Vitória Souza do Nascimento')

#Exibe o menu para o cliente:
print('''
-------------Bem-vindos a Loja de Marmitas da Vitória Souza do Nascimento-------------
------------------------------------CARDAPIO------------------------------------------            
--------------------------------------------------------------------------------------
-----------|  Tamanho  |  Bife Acebolado (BA)  |  Filé de Frango (FF)  |--------------
-----------|     P     |       R$ 16           |       R$ 15           |--------------
-----------|     M     |       R$ 18           |       R$ 17           |--------------
-----------|     G     |       R$ 22           |       R$ 21           |--------------
--------------------------------------------------------------------------------------
''')

#Inicia no acumulador para somar os valores dos pedidos:
total_pedido = 0

while True:  
   
    sabor = input('Digite o sabor (BA/FF): ').strip().upper()
    if sabor not in ['BA', 'FF']:
        print('Sabor inválido. Tente novamente.')
        continue  

    
    tamanho = input('Digite o tamanho (P/M/G): ').strip().upper()
    if tamanho not in ['P', 'M', 'G']:
        print('Tamanho inválido. Tente novamente.')
        continue  

    
    if sabor == 'BA':
        if tamanho == 'P':
            preco = 16
        elif tamanho == 'M':
            preco = 18
        elif tamanho == 'G':
            preco = 22
    elif sabor == 'FF':
        if tamanho == 'P':
            preco = 15
        elif tamanho == 'M':
            preco = 17
        elif tamanho == 'G':
            preco = 21

    total_pedido += preco  
    print(f'Você pediu uma marmita de {sabor} tamanho {tamanho} por R$ {preco:.2f}.')

    mais_pedidos = input('Deseja pedir mais alguma coisa? (S/N): ').strip().upper()
    if mais_pedidos == 'N':
        break  

print(f'Total do pedido: R$ {total_pedido:.2f}')
