# 📦 Projeto 09 — Sistema de Controle de Estoque

Sistema de controle de estoque desenvolvido em **Python**, utilizando um arquivo **JSON** como forma de persistência dos dados.

O projeto foi desenvolvido como parte da minha jornada de aprendizado em Python, com foco em praticar operações CRUD, manipulação de arquivos, validação de dados e organização do código através de funções.

---

## 🎯 Objetivo

Criar um sistema simples de controle de estoque capaz de cadastrar, consultar, alterar e remover produtos, mantendo os dados salvos mesmo após o encerramento do programa.

---

## ⚙️ Funcionalidades

* ➕ Adicionar produtos
* 📋 Listar produtos cadastrados
* 🔎 Buscar produtos
* ✏️ Alterar produtos
* 🗑️ Remover produtos
* 💰 Calcular o valor total de cada produto em estoque
* 📊 Calcular o valor total do estoque
* 💾 Persistir os dados em arquivo JSON
* ✅ Validar entradas do usuário
* 🚫 Impedir valores inválidos para quantidade e preço
* 📁 Verificar a existência do arquivo de dados
* 🆕 Criar o arquivo JSON quando necessário

---

## 🧠 Conceitos praticados

* Variáveis e tipos de dados
* Estruturas condicionais
* Estruturas de repetição
* Funções
* Listas e dicionários
* `while` e `for`
* `try` / `except`
* Validação de entrada
* Manipulação de strings
* Expressões Regulares (Regex)
* Manipulação de arquivos
* `pathlib`
* JSON
* `json.load()`
* `json.dump()`
* Enumeração com `enumerate()`
* Operações CRUD
* Formatação de valores

---

## 💾 Persistência dos dados

Os produtos são armazenados no arquivo:

`DataBase.json`

Cada produto possui as seguintes informações:

```json
{
    "produto": "Arroz",
    "quantidade": 10,
    "preco": 5.99
}
```

Dessa forma, os dados continuam disponíveis mesmo depois que o programa é encerrado.

---

## 🛠️ Tecnologias utilizadas

* 🐍 Python 3
* 📄 JSON
* 🔧 Git
* 🐙 GitHub
* 💻 Visual Studio Code

---

## 📚 Sobre o projeto

Este projeto representa uma evolução em relação aos projetos anteriores, principalmente pela utilização de **persistência de dados em arquivo** e pela implementação de um sistema CRUD completo.

Durante o desenvolvimento também foram trabalhadas diversas validações para evitar entradas inválidas e melhorar a experiência de utilização do programa.

O projeto foi desenvolvido buscando resolver os problemas de forma independente, utilizando documentação e ferramentas de consulta como apoio durante o aprendizado.

---

## 🚀 Próximos passos

A próxima etapa da evolução será substituir o armazenamento em JSON por um **banco de dados SQLite**, permitindo praticar conceitos de banco de dados e consultas SQL dentro de uma aplicação Python.

---

⭐ Projeto desenvolvido como parte da minha jornada de aprendizado em Python.
