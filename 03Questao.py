# 3. Verificação de Idade para Acesso
# • Descrição: Desenvolva um programa que peça a idade do usuário e informe se ele é maior
# ou menor de idade.
# • Comandos utilizados: input(), if, else, print().

# Solicitar a idade do usuário
idade = int(input("Digite sua idade: "))

# Verificar se o usuário é maior ou menor de idade
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")