#Inicialização de variáveis:
id_global = 4297913 

#lista de dicionários:
lista_funcionarios = []

#Função para cadastrar um funcionário:
def cadastrar_funcionario():
    global id_global 
    
    print("\n----------- MENU CADASTRAR FUNCIONARIO ---------------")
    id_funcionario = input("Digite o id do funcionário: ")
    
    if id_funcionario == '':
        id_funcionario = id_global
        id_global += 1  
    else:
        id_funcionario = int(id_funcionario)
    
    #Dado do funcionário:
    nome = input("Digite o nome do funcionário: ")
    setor = input("Digite o setor do funcionário: ")
    salario = float(input("Digite o salário do funcionário: "))
    print("""----------------------------------------------------""")
    #Informações do funcionário:
    funcionario = {
        'id': id_funcionario,
        'nome': nome,
        'setor': setor,
        'salario': salario
    }
    print("""----------------------------------------------------""")
    #Adicionando o funcionário à lista:
    lista_funcionarios.append(funcionario.copy())  #copy para evitar referência direta.
    print("Funcionário cadastrado com sucesso!")
    print(  )

#Função para consultar funcionários:
def consultar_funcionarios():
    while True:
        print("""------------ MENU CONSULTAR FUNCIONARIO ---------------""")
        print("1. Consultar Todos os Funcionarios")
        print("2. Consultar Funcionario por Id")
        print("3. Consultar Funcionario(s) por Setor")
        print("4. Retornar")
        opcao = input(">>")
        
        if opcao == '1':
            #Consultar todos os funcionários:
            print("\nTodos os funcionários:")
            for funcionario in lista_funcionarios:
                print(funcionario)
        
        elif opcao == '2':
            #Consultar por Id:
            id_consulta = int(input("Digite o id do funcionário: "))
            encontrado = False
            for funcionario in lista_funcionarios:
                if funcionario['id'] == id_consulta:
                    print("\nFuncionário encontrado:")
                    print(funcionario)
                    encontrado = True
                    break
            if not encontrado:
                print("Funcionário não encontrado.")
        
        elif opcao == '3':
            # Consultar por Setor
            setor_consulta = input("Digite o setor a ser consultado: ")
            encontrados = []
            for funcionario in lista_funcionarios:
                if funcionario['setor'].lower() == setor_consulta.lower():
                    encontrados.append(funcionario)
            
            if encontrados:
                print("\nFuncionários no setor", setor_consulta + ":")
                for funcionario in encontrados:
                    print(funcionario)
            else:
                print("Nenhum funcionário encontrado neste setor.")
        
        elif opcao == '4':
            # Retornar ao menu principal
            return
        
        else:
            print("Opção inválida.")

# Função para remover um funcionário
def remover_funcionario():
    while True:
        print("""------------ MENU REMOVER FUNCIONARIO ---------------""")
        id_remover = int(input("Digite o id do funcionário a ser removido: "))
        encontrado = False
        for funcionario in lista_funcionarios:
            if funcionario['id'] == id_remover:
                lista_funcionarios.remove(funcionario)
                print("Funcionário removido com sucesso.")
                encontrado = True
                break
        if encontrado:
            # Se encontrou e removeu o funcionário, sai do loop
            break
        else:
            print("Id inválido. Funcionário não encontrado.")

# Menu principal do programa
while True:
    print(''' Bem-vindos a empresa da Vitória Souza do Nascimento
-------------------------------------------------------
----------------- MENU PRINCIPAL ----------------------''')
    print("Escolha a opção desejada:")
    print("1 - Cadastrar Funcionário")
    print("2 - Consultar Funcionário(s)")
    print("3 - Remover Funcionário")
    print("4 - Sair")
    opcao_menu = input(">>")
    print("""--------------------------------------------------------""")
    if opcao_menu == '1':
        # Cadastrar funcionário
        cadastrar_funcionario()
    
    elif opcao_menu == '2':
        # Consultar funcionários
        consultar_funcionarios()
    
    elif opcao_menu == '3':
        # Remover funcionário
        remover_funcionario()
    
    elif opcao_menu == '4':
        # Encerrar o programa
        print("Encerrando o programa...")
        break
    
    else:
        print("Opção inválida. Escolha uma opção de 1 a 4.")
