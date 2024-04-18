lista = []
executando = True

while executando:
    menu = '''
        DIGITE QUAL OPÇÃO DESEJA UTILIZAR:
        (1) Cadastrar novo usuário
        (2) Cadastrar novo veículo
        (3) Relatar problema
        (4) Pedir guincho
        (X) Sair do sistema
        
    '''

    print(menu)
    opcao = input().lower()[0]

    if opcao == '1':
        cadastrar = {}
        cadastrar["nome"] = input("\nDigite o nome completo: ")
        cadastrar["data"] = input("Digite a data de nascimento: ")
        cadastrar["rg"] = input("Digite o seu RG: ")
        cadastrar["cpf"] = input("Digite seu CPF: ")
        print("\nParabéns,", cadastrar["nome"], "você concluiu seu cadastro com sucesso!")
        lista.append(cadastrar)
    if opcao == '2':
        cadastrar = {}
        cadastrar["tipo"] = input("\nDigite o tipo de veículo(Carro, Moto, Caminhão, Bicicleta): ")
        cadastrar["modelo"] = input("Digite o nome e marca do veículo: ")
        cadastrar["cor"] = input("Digite a cor do veículo : ")
        cadastrar["ano"] = input("Informe o ano do veículo: ")
        print("\nParabéns, seu veículo", cadastrar["modelo"], "foi cadastrado com sucesso!")
        lista.append(cadastrar)
    elif opcao == '3':
        problema = {}
        problema["problema"] = input("\nInforme qual o problema: ")
        print("\nOk! Venha até a nossa oficina para solucionarmos o seu problema \nou entre em contato com o guincho digitando a opção de número 4!")
        lista.append(problema)
    elif opcao == '4':
        guincho = {}
        guincho["endereco"] = input("\nInforme qual endereço: ")
        print("\nPerfeito! Em breve chegaremos ao endereço:", guincho["endereco"])
        
    elif opcao == 'x':
        print("\nObrigado por utilizar nosso sistema. Sempre que precisar, estaremos a disposição!😊")
        executando = False
print("\n")
