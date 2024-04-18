lista = []
executando = True

print("\nOlá! Antes de começar, precisamos que você realize o cadastro abaixo:")
cadastrar = {}
cadastrar["nome"] = input("\nDigite o seu nome completo: ")
cadastrar["data"] = input("Digite a sua data de nascimento: ")
cadastrar["rg"] = input("Digite o seu RG: ")
cadastrar["cpf"] = input("Digite seu CPF: ")
print("\nParabéns,", cadastrar["nome"], "você concluiu seu cadastro com sucesso!")
lista.append(cadastrar)

while executando:
    menu = '''
        DIGITE QUAL OPÇÃO DESEJA UTILIZAR:
        (1) Cadastrar novo veículo
        (2) Relatar problema
        (3) Pedir guincho
        (X) Sair do sistema
        \n
    '''

    print(menu)
    opcao = input().lower()[0]

    if opcao == '1':
        cadastrar = {}
        cadastrar["tipo"] = input("Digite o tipo de veículo(Carro, Moto, Caminhão, Bicicleta): ")
        cadastrar["modelo"] = input("Digite o nome e marca do veículo: ")
        cadastrar["cor"] = input("Digite a cor do veículo: ")
        cadastrar["ano"] = input("Informe o ano do veículo: ")
        print("Parabéns, seu veículo", cadastrar["modelo"], "foi cadastrado com sucesso!")
        lista.append(cadastrar)
    elif opcao == '2':
        problema = {}
        problema["problema"] = input("Informe qual o problema: ")
        print("\n\nOk! Venha até a nossa oficina para solucionarmos o seu problema \nou entre em contato com o guincho digitando a opção de número 3!")
        lista.append(problema)
    elif opcao == '3':
        guincho = {}
        guincho["endereco"] = input("Informe qual endereço: ")
        print("Perfeito! Em breve chegaremos ao endereço:",guincho["endereco"])
        
    elif opcao == 'x':
        print("\nObrigado por utilizar nosso sistema. Sempre que precisar, estaremos a disposição!😊")
        executando = False
print("\n")