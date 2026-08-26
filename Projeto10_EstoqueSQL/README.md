# 🗃️ Projeto 10 — Sistema de Estoque com SQLite

Sistema de gerenciamento de estoque desenvolvido em **Python**, utilizando **SQLite** para armazenamento persistente dos dados.

Este projeto representa uma evolução do sistema de estoque desenvolvido anteriormente com arquivos JSON. Nesta versão, os produtos são armazenados em um banco de dados relacional, permitindo praticar conceitos básicos de SQL e integração entre Python e SQLite.

---

## 🎯 Objetivo

Desenvolver um sistema de estoque em terminal capaz de realizar as principais operações de gerenciamento de produtos:

* Cadastrar produtos
* Listar produtos
* Buscar produtos
* Alterar informações
* Remover produtos
* Armazenar os dados de forma persistente em um banco de dados

---

## ⚙️ Funcionalidades

### ➕ Adicionar produto

Permite cadastrar:

* Nome do produto
* Quantidade
* Preço

O sistema realiza validações dos dados informados e impede o cadastro de produtos duplicados.

### 📋 Listar produtos

Exibe os produtos cadastrados e calcula:

* Valor individual em estoque
* Quantidade total de produtos
* Valor total do estoque

### 🔎 Buscar produto

Permite localizar um produto cadastrado pelo nome e visualizar suas informações.

### ✏️ Alterar produto

Permite modificar:

* Nome
* Quantidade
* Preço

### 🗑️ Remover produto

Permite selecionar um produto pelo seu ID e removê-lo do banco de dados.

---

## 🗄️ Banco de Dados

O projeto utiliza **SQLite** através do módulo `sqlite3` do Python.

A tabela `produtos` possui a seguinte estrutura:

| Campo        | Tipo    | Descrição             |
| ------------ | ------- | --------------------- |
| `id`         | INTEGER | Identificador único   |
| `produto`    | TEXT    | Nome do produto       |
| `quantidade` | INTEGER | Quantidade disponível |
| `preco`      | FLOAT   | Preço do produto      |

O ID é gerado automaticamente através de `AUTOINCREMENT`.

---

## 🧠 Conceitos praticados

* Python
* Funções
* Estruturas condicionais
* Estruturas de repetição
* Listas e tuplas
* Tratamento de exceções com `try/except`
* Validação de entrada
* Manipulação de dados
* SQLite
* SQL
* `SELECT`
* `INSERT`
* `UPDATE`
* `DELETE`
* `fetchall()`
* `fetchone()`
* `commit()`
* `close()`
* CRUD
* Chaves primárias
* Persistência de dados
* Queries parametrizadas

---

## 🛠️ Tecnologias utilizadas

* 🐍 Python 3
* 🗃️ SQLite
* 💻 VS Code
* 🔧 Git
* 🐙 GitHub

---

## 📚 Evolução do projeto

Este projeto faz parte da minha jornada de aprendizado em Python.

A versão anterior do sistema utilizava um arquivo JSON para armazenar os produtos. Nesta versão, o armazenamento foi substituído por um banco de dados SQLite, permitindo praticar conceitos de bancos de dados e operações SQL.

A ideia é evoluir gradualmente os projetos, aplicando os conceitos aprendidos em projetos anteriores e introduzindo novas tecnologias conforme avanço nos estudos.

---

## 🚀 Próximos passos

Continuar aprofundando os conhecimentos em:

* SQL
* Bancos de dados relacionais
* Organização e modularização de projetos
* APIs
* Desenvolvimento de aplicações maiores
* Interfaces gráficas
* Integração entre diferentes tecnologias

---

⭐ Este projeto faz parte do meu portfólio de estudos e representa mais uma etapa da minha evolução na programação.
