# 11. Cadastro de Alunos
# • Descrição: Desenvolva um sistema de cadastro de alunos onde o usuário pode inserir nome,
# idade e nota. Armazene essas informações em um dicionário e exiba os dados cadastrados.
# • Comandos utilizados: input(), print(), dicionários, for.

def menu ():
    print("""
    ----------------------------
    |                          |
    |      Tela de Login       |
    |                          |
    |  1. Cadastrar Senha      |
    |  2. Fazer Login          |
    |                          |
    ----------------------------
    \n""")


menu()


opcao = int(input("Escolha uma opção: "))
senha = ""


def cadastrar_senha (senha):
     # Cadastrar uma senha
    if opcao == 1:
        senha_cadastrada = input("Cadastre uma senha: ")
        confirmacao_senha = input("Confirme sua senha: ")


        while senha_cadastrada != confirmacao_senha:
            print("As senhas estão diferentes, tente novamente!")
            senha_cadastrada = input("Cadastre uma senha: ")
            confirmacao_senha = input("Confirme sua senha: ")


        senha = senha_cadastrada


        print("Senha cadastrada com sucesso!")


    # Solicitar que o usuário faça login
    if opcao == 2:
        if senha != "":
            senha_login = input("Digite sua senha: ")
            if senha_login == senha:
                    print("Você logou com sucesso!")
            while senha_login != senha:
                senha_login = input("Digite sua senha: ")
        else:
            print("Nenhuma senha cadastrada!")
           
