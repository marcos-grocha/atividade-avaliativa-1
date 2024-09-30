# Projeto de Questões em Python

Este repositório contém três programas desenvolvidos em Python, que abordam diferentes funcionalidades, organizadas nas **Questões 03, 11 e 20**.

## Sumário

- [Questão 03: Verificar Maioridade](#questão-03-verificar-maioridade)
- [Questão 11: Cadastro de Alunos](#questão-11-cadastro-de-alunos)
- [Questão 20: Sistema de Login e Senha](#questão-20-sistema-de-login-e-senha)
- [Requisitos](####requisitos)
- [Como rodar o código](#como-rodar-o-código)
- [Autor](####autor)

---

## Questão 03: Verificação de Idade para Acesso

## Descrição
Este é um programa simples que solicita ao usuário a sua idade e informa se ele é maior ou menor de idade. 
O objetivo é praticar o uso de estruturas condicionais (`if/else`) e interação com o usuário via `input()` e `print()`.

### Funcionalidades
- O programa solicita que o usuário insira a sua idade.
- Verifica se o usuário tem 18 anos ou mais para determinar se é maior de idade.
- Exibe uma mensagem indicando se o usuário é maior ou menor de idade.

### Como Executar
1. Certifique-se de ter o Python instalado em sua máquina.
2. Baixe o código ou copie para um arquivo `idade_verificacao.py`.
3. Execute o código com o seguinte comando no terminal:

   ```bash
   python idade_verificacao.py

### Exemplo de uso
----------------------------------------------------------------------  
| Olá! Nosso programa te ajuda a descobrir se você é maior de idade...  
| Digite sua idade: 20  
| Você tem 20 anos, portanto é MAIOR de idade.  
----------------------------------------------  
=== Obrigado por usar nosso aplicativo! ===

---

## Questão 11: Sistema de Cadastro de Alunos

### Descrição
Este programa permite o cadastro de alunos, onde o usuário pode inserir o nome, idade e nota de cada aluno. 
As informações são armazenadas em um dicionário e, ao final, o sistema exibe todos os dados cadastrados.

### Funcionalidades
- Solicita o número de alunos a serem cadastrados.
- Permite inserir nome, idade e nota de cada aluno.
- Armazena as informações em um dicionário, com o nome como chave e a idade e nota como valores.
- Exibe os dados de todos os alunos cadastrados.

### Como Executar
1. Certifique-se de ter o Python instalado em sua máquina.
2. Copie o código para um arquivo `cadastro_alunos.py`.
3. Execute o código com o seguinte comando no terminal:

   ```bash
   python cadastro_alunos.py

### Exemplo de uso
Quantos alunos deseja cadastrar: 2

Cadastro do aluno 1:
   Nome: João
   Idade: 20
   Nota: 8.5

Cadastro do aluno 2:
   Nome: Maria
   Idade: 19
   Nota: 9.2

Alunos cadastrados:
   Nome: João, Idade: 20, Nota: 8.5
   Nome: Maria, Idade: 19, Nota: 9.2
   
=== Obrigado por usar nosso aplicativo! ===

---

## Questão 20: Sistema de Verificação de Senha

### Descrição
Este programa é um sistema simples de verificação de senha. 
O usuário pode cadastrar uma senha e, em seguida, fazer login com a senha cadastrada. 
Se a senha estiver correta, o acesso é concedido. Caso contrário, uma mensagem de erro é exibida. 
O sistema inclui um menu que oferece as opções de cadastrar senha, fazer login ou sair do programa.

### Funcionalidades
- **Cadastrar Senha**: Permite ao usuário cadastrar uma senha com confirmação.
- **Fazer Login**: O usuário insere a senha cadastrada e, se for válida, o acesso é concedido.
- **Menu**: Interface simples que permite navegar entre as opções de cadastrar senha, fazer login ou sair do programa.

### Como Executar
1. Certifique-se de ter o Python instalado em sua máquina.
2. Copie o código para um arquivo `verificacao_senha.py`.
3. Execute o código com o seguinte comando no terminal:

   ```bash
   python verificacao_senha.py

### Exemplo de uso
Vamos cadastrar uma senha...

   Cadastre uma senha: 1234
   Confirme sua senha: 1234
   
   Senha cadastrada com sucesso.

Digite sua senha: 1234

 === SUCESSO ao fazer login! ===

---

#### Requisitos: Python 3.x
#### Este projeto não possui uma licença específica. Sinta-se à vontade para usar e modificar como desejar.
#### Autor: marcos-grocha
