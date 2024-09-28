# 20. Verificação de Senha
# • Descrição: Crie um sistema de verificação de senha onde o usuário insere a senha e, se ela
# estiver correta, o acesso é concedido. Caso contrário, exiba uma mensagem de erro.
# • Comandos utilizados: input(), if, else, print().

senha = ""

def verificar_senha(senha_cadastrada, confirmacao_senha):
    while senha_cadastrada != confirmacao_senha:
        print("As senhas estão diferentes, digite novamente")
        senha_cadastrada = input("Digite sua senha: ")
        confirmacao_senha = input("Confirme sua senha: ")
    return senha_cadastrada


def cadastrar_senha():
   
    return senha


def login():
    if senha != "":
        possivel_senha = input("Digite sua senha: ")
        if senha == possivel_senha:
            print("Você fez login com sucesso!")
        else:
            print("Senha inválida")
            menu()
    else:
        print("Nenhuma senha cadastrada!")
        menu()
       
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
   
opcao = menu()
if opcao == 1:
    senha_nova = verificar_senha(input("Cadastre uma senha: "), input("Confirme sua senha: "))
    print("Senha cadastrada com sucesso")
    senha = senha_nova
elif opcao == 2:
    login()
elif opcao == 3:
    print("Saindo...")
    exit()
else:
    print("Opção inválida.")
    login()
