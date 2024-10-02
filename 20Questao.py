
# Variável global
senha = ""

# Método para cadastrar uma senha
def cadastrar_senha():
    global senha
    senha_escolhida = input("Cadastre uma senha: ")
    senha_confirmada = input("Confirme sua senha: ")
    while senha_escolhida != senha_confirmada:
        print("As senhas estão diferentes, digite novamente")
        senha_escolhida = input("Digite sua senha: ")
        senha_confirmada = input("Confirme sua senha: ")
    senha = senha_escolhida
    print("Senha cadastrada com sucesso.")

# Método para fazer login
def login():
    if senha != "":
        possivel_senha = input("Digite sua senha: ")
        if senha == possivel_senha:
            print("\n === SUCESSO ao fazer login! ===\n")
        else:
            print("\n --- Senha inválida. ---\n")
    else:
        print("\n (!) Nenhuma senha cadastrada! Cadastre uma senha primeiro. (!)")
       
# Metódo que monta o menu e aguarda resposta do usuário
def menu():
    print("""   |  =  Menu Inicial  =  |
                | [1] Cadastrar Senha  |
                | [2] Fazer Login      |
                | [3] Sair             |\n """)
    opcao = int(input("Escolha uma opção: "))
    return opcao

# Validação da opção escolhida pelo usuário
while True:
    opcao = menu()
    if opcao == 1:
        cadastrar_senha()
    elif opcao == 2:
        login()
    elif opcao == 3:
        print("Saindo...")
        break
    else:
        print("Opção inválida.")