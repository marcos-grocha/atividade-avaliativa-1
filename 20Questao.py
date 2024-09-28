# 20. Verificação de Senha
# • Descrição: Crie um sistema de verificação de senha onde o usuário insere a senha e, se ela
# estiver correta, o acesso é concedido. Caso contrário, exiba uma mensagem de erro.
# • Comandos utilizados: input(), if, else, print().

# Definir a senha correta
senha_correta = "senha123"

# Solicitar que o usuário insira a senha
senha_usuario = input("Digite sua senha: ")

# Verificar se a senha inserida está correta
if senha_usuario == senha_correta:
    print("Acesso concedido.")
else:
    print("Senha incorreta. Acesso negado.")