
# Inicializando um dicionário vazio para armazenar os alunos
cadastro_alunos = {}

# Definir quantos alunos serão cadastrados
numero_alunos = int(input("Quantos alunos deseja cadastrar: "))

# Loop para cadastrar os alunos
for i in range(numero_alunos):
    print(f"\nCadastro do aluno {i+1}:")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    nota = float(input("Nota: "))
   
    # Armazenar as informações do aluno no dicionário
    cadastro_alunos[nome] = { "Idade": idade, "Nota": nota }

# Exibir os dados cadastrados
print("\nAlunos cadastrados:")
for nome, dados in cadastro_alunos.items():
    print(f"Nome: {nome}, Idade: {dados['Idade']}, Nota: {dados['Nota']}")