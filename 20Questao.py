# 20. Verificação de Senha
# • Descrição: Crie um sistema de verificação de senha onde o usuário insere a senha e, se ela
# estiver correta, o acesso é concedido. Caso contrário, exiba uma mensagem de erro.
# • Comandos utilizados: input(), if, else, print().

senha = ""
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

def login():
    if senha != "":
        possivel_senha = input("Digite sua senha: ")
        if senha == possivel_senha:
            print("\n === SUCESSO ao fazer login! ===\n")
        else:
            print("\n --- Senha inválida. ---\n")
    else:
        print("\n (!) Nenhuma senha cadastrada! Cadastre uma senha primeiro. (!)")
       
def menu():
    print("""
    |----------------------|
    |  =  Menu Inicial  =  |
    |                      |
    | [1] Cadastrar Senha  |
    | [2] Fazer Login      |
    | [3] Sair             |
    |                      |
    |----------------------|\n
    """)
    opcao = int(input("Escolha uma opção: "))
    return opcao

while True:
    opcao = menu()
    if opcao == 1:
        print("Vamos cadastrar uma senha...")
        cadastrar_senha()
        login()
    elif opcao == 2:
        print("Vamos fazer login...")
        login()
    elif opcao == 3:
        print("\n=== Obrigado por usar nosso aplicativo! ===")
        print("__________________________________Saindo...")
        break
    else:
        print("Opção inválida.")
