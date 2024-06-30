#Função para escolher o modelo de camiseta:
def escolha_modelo():
    while True:
        modelo = input("Escolha o modelo de camiseta: \n MCS - Manga Curta Simples \n MLS - Manga Longa Simples \n MCE - Manga Curta Com Estampa \n MLE - Manga Longa Com Estampa \n >> ").strip().upper()
        if modelo in ['MCS', 'MLS', 'MCE', 'MLE']:
            #Retorna o valor do modelo:
            if modelo == 'MCS':
                return 1.80
            elif modelo == 'MLS':
                return 2.10
            elif modelo == 'MCE':
                return 2.90
            elif modelo == 'MLE':
                return 3.20
        else:
            print("Opção inválida. Escolha entre MCS, MLS, MCE ou MLE.")

#Função de pergunta e calculo do número de camisetas com desconto:
def num_camisetas():
    while True:
        try:
            num = int(input("Digite o número de camisetas desejado: "))
            if num > 20000:
                print("Não é possível realizar pedidos acima de 20000 camisetas.")
            elif num < 20:
                return num  # Sem desconto
            elif num < 200:
                return int(num * 0.95)  #5%
            elif num < 2000:
                return int(num * 0.93)  #7%
            else:
                return int(num * 0.88)  #12%
        except ValueError:
            print("Valor inválido. Digite um número inteiro.")

#Função para escolher o tipo de frete:
def frete():
    while True:
        try:
            opcao = int(input("Escolha o tipo de frete: \n  0 - Retirar na fábrica (R$ 0.00)\n  1 - Transportadora (R$ 100.00)\n  2 - Sedex (R$ 200.00)\nDigite o número correspondente: "))
            if opcao in [0, 1, 2]:
                if opcao == 0:
                    return 0.00
                elif opcao == 1:
                    return 100.00
                elif opcao == 2:
                    return 200.00
            else:
                print("Opção inválida. Escolha 0, 1 ou 2.")
        except ValueError:
            print("Opção inválida. Digite um número.")

#Parte principal do programa:
print("Bem vindos a Fábrica de Camisetas da Vitória Souza do Nascimento")

try:
    #Chamada das funções:
    valor_modelo = escolha_modelo()
    quantidade_camisetas = num_camisetas()
    valor_frete = frete()

    #Calculo do total a pagar:
    subtotal = valor_modelo * quantidade_camisetas
    total = subtotal + valor_frete

    #Exibe o total do pedido:
    print("\nResumo do Pedido:")
    print(f"Modelo escolhido: Valor por unidade = R$ {valor_modelo:.2f}")
    print(f"Número de camisetas com desconto: {quantidade_camisetas}")
    print(f"Subtotal: R$ {subtotal:.2f}")
    print(f"Valor do frete: R$ {valor_frete:.2f}")
    print(f"TOTAL: R$ {total:.2f} (MODELO: {valor_modelo:.2f} * QUANTIDADE(COM DESCONTO): {quantidade_camisetas} + FRETE: {valor_frete:.2f})")

except KeyboardInterrupt:
    print("\nPrograma interrompido pelo usuário.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
