# 📦 Projeto 08 - Sistema de Estoque com Persistência em Arquivo

Este projeto foi desenvolvido como parte da minha jornada de estudos em Python.

O objetivo foi evoluir o sistema de estoque criado anteriormente, substituindo o armazenamento em listas pelo armazenamento permanente em um arquivo `.txt`.

Foi meu primeiro projeto utilizando leitura e escrita de arquivos, permitindo que os produtos permaneçam salvos mesmo após o encerramento do programa.

---

## 🚀 Funcionalidades

- ✅ Adicionar produtos
- ✅ Listar todos os produtos
- ✅ Buscar produtos por nome
- ✅ Alterar nome, quantidade ou preço
- ✅ Remover produtos
- ✅ Persistência de dados em arquivo `.txt`
- ✅ Validação de entradas do usuário
- ✅ Cálculo do valor total por produto
- ✅ Cálculo do valor total do estoque
- ✅ Tratamento de opções inválidas

---

## 🛠️ Tecnologias utilizadas

- Python 3
- Manipulação de arquivos (`open`)
- pathlib
- Expressões Regulares (`re`)
- Funções (`def`)
- Listas
- Strings
- Loops (`for` / `while`)
- Condicionais (`if`)
- `enumerate()`
- `split()` e `join()`
- `readlines()` e `writelines()`
- Tratamento de exceções (`try/except`)

---

## 📂 Estrutura do arquivo

Os produtos são armazenados no arquivo `DataBase.txt` utilizando o formato:

Mouse;10;89.90
Teclado;5;199.90
Monitor;3;899.90

Cada linha representa um produto contendo:

- Nome
- Quantidade
- Preço

---

## 💻 O que aprendi

Durante este projeto pratiquei diversos conceitos importantes:

- Organização do código utilizando funções
- Persistência de dados em arquivos
- Leitura e escrita de arquivos texto
- Atualização de registros utilizando listas temporárias
- Exclusão de registros
- Manipulação de strings
- Conversão entre tipos (`int`, `float` e `str`)
- Tratamento de erros com `try/except`
- Separação de responsabilidades entre funções

---

## 📈 Evolução

Este projeto representa uma evolução importante em relação aos anteriores.

Enquanto os projetos anteriores armazenavam todas as informações apenas na memória utilizando listas, este sistema mantém os dados gravados em arquivo, permitindo que as informações permaneçam disponíveis entre diferentes execuções do programa.

Esse foi meu primeiro contato com persistência de dados em Python e servirá de base para os próximos projetos utilizando JSON, SQLite e Banco de Dados.

---

## 🎯 Próximos passos

- Armazenamento em JSON
- Programação Orientada a Objetos (POO)
- Banco de Dados SQLite
- APIs
- Desenvolvimento de Chatbots