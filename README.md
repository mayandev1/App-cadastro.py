# README - Sistema de Gerenciamento de Usuários e Produtos

## Visão Geral
Este é um sistema simples de gerenciamento de usuários e produtos utilizando **SQLite** para armazenamento de dados e **bcrypt** para hashing de senhas. O sistema permite:

- Registro e login de usuários.
- Adição, listagem e remoção de produtos.
- Proteção de senhas com hashing seguro.
- Interface de linha de comando interativa.

## Tecnologias Utilizadas
- **Python** (para lógica do sistema)
- **SQLite** (para banco de dados local)
- **bcrypt** (para hashing de senhas)
- **getpass** (para entrada segura de senhas)

## Estrutura do Código
### 1. Configuração Inicial
O sistema inicia criando um banco de dados SQLite chamado `usuarios.db`, que contém duas tabelas:

- **usuarios**: Armazena os dados de login (ID, nome de usuário e senha criptografada).
- **produtos**: Armazena informações sobre produtos (ID, nome, preço e quantidade).

### 2. Registro de Usuários
Os usuários podem se registrar fornecendo:
- Nome de usuário (deve ser único).
- Senha (armazenada de forma segura com bcrypt).

Se o nome de usuário já existir, o registro falha.

### 3. Login de Usuários
Os usuários devem inserir:
- Nome de usuário.
- Senha (validada comparando o hash salvo no banco de dados).

Se as credenciais forem corretas, o usuário ganha acesso ao sistema de gerenciamento de produtos.

### 4. Gerenciamento de Produtos
Após o login, o usuário pode:
- **Adicionar produtos** informando nome, preço e quantidade.
- **Listar produtos** armazenados no banco de dados.
- **Remover produtos** pelo ID.

## Como Executar o Programa
### 1. Instalar Dependências
Certifique-se de ter **Python 3** instalado e instale o bcrypt:
```bash
pip install bcrypt
```

### 2. Executar o Programa
Para iniciar o sistema, execute:
```bash
python nome_do_arquivo.py
```

### 3. Fluxo de Uso
1. Escolha `1` para **registrar um novo usuário**.
2. Escolha `2` para **fazer login**.
3. Após o login, escolha opções para **gerenciar produtos**.
4. Escolha `3` para **sair do sistema**.

## Segurança
- Senhas são criptografadas com bcrypt antes de serem armazenadas.
- O sistema impede que nomes de usuário duplicados sejam registrados.
- O `getpass.getpass()` impede que senhas sejam exibidas durante a digitação.

## Possíveis Melhorias
- Implementar autenticação com sessões.
- Criar uma interface gráfica (GUI).
- Melhorar o sistema de permissões para diferentes tipos de usuários.

## Autor
Desenvolvido como um sistema simples para gestão de usuários e produtos com armazenamento local seguro.
