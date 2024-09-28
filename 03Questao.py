# 3. Verificação de Idade para Acesso
# • Descrição: Desenvolva um programa que peça a idade do usuário e informe se ele é maior
# ou menor de idade.
# • Comandos utilizados: input(), if, else, print().

# Solicitar a idade do usuário
print("----------------------------------------------------------------------")
print("| Olá! Nosso programa te ajuda a descobrir se você é maior de idade...")
idade = int(input("| Digite sua idade: "))

# Verificar se o usuário é maior ou menor de idade
if idade >= 18:
    print(f"| Você tem {idade} anos, portanto é MAIOR de idade.")
    print("----------------------------------------------")
else:
    print(f"| Você tem {idade} anos, portanto é MENOR de idade.")
    print("----------------------------------------------")
print("=== Obrigado por usar nosso aplicativo! ===\n")