
print('Bem-vindos à loja da Vitória Souza do Nascimento')

valorPedido = float(input('Digite o valor do pedido:' ))
quantidadeParcelas = int(input('Digite a quantidade de parcelas: '))

# Inicializando a variável de juros:
juros = 0

if quantidadeParcelas < 4:
    juros = 0  
elif 4 <= quantidadeParcelas < 6:
    juros = 4 / 100  
elif 6 <= quantidadeParcelas < 9:
    juros = 8 / 100  
elif 9 <= quantidadeParcelas < 13:
    juros = 16 / 100  
else:
    juros = 32 / 100  

#Calculando o valor da parcela:
valorParcela = valorPedido * (1 + juros) / quantidadeParcelas

#Calculando o valor total parcelado:
totalParcelado = valorParcela * quantidadeParcelas

print('Vitória Souza do Nascimento')

#Ele verifica se existe juros para exibir a mensagem de parcelamento com juros!
if quantidadeParcelas >= 4:
    print(f'Parcelamento com Juros: \n Valor da Parcela: R$ {valorParcela:.2f} \nValor Total Parcelado: R$ {totalParcelado:.2f}')