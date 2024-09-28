# 11. Cadastro de Alunos
# • Descrição: Desenvolva um sistema de cadastro de alunos onde o usuário pode inserir nome,
# idade e nota. Armazene essas informações em um dicionário e exiba os dados cadastrados.
# • Comandos utilizados: input(), print(), dicionários, for.

# Inicializando um dicionário vazio para armazenar os alunos
cadastro_alunos = {}


# Definir quantos alunos serão cadastrados
print("\n================================")
numero_alunos = int(input("Quantos alunos deseja cadastrar: "))
print("================================")

# Loop para cadastrar os alunos
for i in range(numero_alunos):
    print(f"\nCadastro do aluno {i+1}:")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    nota = float(input("Nota: "))
   
    # Armazenar as informações do aluno no dicionário
    cadastro_alunos[nome] = {
        "Idade": idade,
        "Nota": nota
    }

# Exibir os dados cadastrados
print("\nAlunos cadastrados:")
for nome, dados in cadastro_alunos.items():
    print(f"Nome: {nome}, Idade: {dados['Idade']}, Nota: {dados['Nota']}")
print("=== Obrigado por usar nosso aplicativo! ===\n")