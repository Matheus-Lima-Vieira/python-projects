#json.load() para ler o arquivo
#json.dump() para gravar o arquivo
import os
import re
import json
from pathlib import Path

selecao = ()
db = "DataBase.json"
DataBase = Path(db)

def arquivo_existe():
    if DataBase.is_file():
        print(f"Arquivo '{DataBase}' encontrado!\n")
        return True
    else:
        print(f"O arquivo '{DataBase}' não foi encontrado!")
        opcao = input("Deseja criar esse arquivo? (s/n): ").strip().lower()

    if opcao == "s":
        with open(DataBase, "w", encoding="utf-8") as db:
            json.dump([], db)
        print(f"Arquivo '{DataBase}' criado com sucesso")
        return True
    else:
        print("Operação cancelada. O arquivo não foi criado.")
        return False

def menu(): 
    print("1 - Adicionar produto\n" \
        "2 - Listar produtos\n" \
        "3 - Buscar produto\n" \
        "4 - Alterar produto\n" \
        "5 - Remover produto\n" \
        "6 - Sair\n")

def cabecalho():
    print("======= ESTOQUE =======")

def encerrar():
    print("\nEncerrando o sistema")

def adicionar_produto():
    if not arquivo_existe():
        return
    #Abre o arquivo Json
    with open(db, "r+", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)
        #Loop do adicionar produto
        while True:
            cabecalho()
            #Lopp para pedir o produto
            while True:
                produto = input("Qual produto deseja adicionar?\n").title()
                #Valida se o usuário digitou somente letras e espaços
                if all(caractere.isalpha() or caractere.isspace() for caractere in produto):
                    break
                else:
                    print("Digite apenas letras")
            #Loop para pedir o produto
            while True:
                #Valida se foi digitando um int
                try:
                    quantidade = int(input("Qual a quantidade desse produto?\n"))
                    break
                except ValueError:
                    print("Digite apenas números")
            #Loop para pedir o valor
            while True:
                #Valida se foi digitado um valor float
                try:
                    preco = float(input("Qual o valor do produto? \n"))
                    break
                except ValueError:
                    print("Digite apenas números")
            dados.append({"produto": produto,
                            "quantidade": quantidade,
                            "preco": preco
                            },)
            arquivo.seek(0)
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)
            arquivo.truncate()
            print("Produto adicionado com sucesso!\n")
            opcao = input("Deseja adicionar mais um produto? S/N\n").strip().lower()
            if opcao != "s":
                break

def listar_produto():
    if not arquivo_existe():
        return
    #valor total de estoque
    estoque_total = 0
    #valor total de cada produto
    total_produtos = 0
    print("==============================")
    with open(db, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)
        if not dados:
            print("Nenhum produto cadastrado!")
        for indice, item in enumerate(dados):
            print(f"{indice+1} - {item['produto']}"
                f"\nQuantidade: {item['quantidade']}"
                f"\nPreço: R$ {item['preco']:.2f}")
            '''
            print(indice+1,"-",item["produto"],
                "\nQuantidade:",item["quantidade"],
                "\nPreço: R$",item["preco"])
            '''
            total_produtos += 1
            valor_produtos = int(item["quantidade"]) * float(item["preco"])
            print(f"Valor em estoque: R${valor_produtos:.2f}\n")
            estoque_total += valor_produtos
    print("==============================")
    print(f"TOTAL DE PRODUTOS: {total_produtos}")
    print(f"VALOR TOTAL: R${estoque_total:.2f}")
    print("==============================")

def buscar_produto():
    if not arquivo_existe():
        return
    cabecalho()
    with open(db, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)
        busca = input("Qual produto deseja procurar? \n").title()
        busca_produto = False
        for item in dados:
            #produto = item
            if busca == item["produto"]:
                busca_produto = True
                total_produto = int(item["quantidade"]) * float(item["preco"])
                print(("\nProduto encontrado!\n") +
                    (f"Produto: {item['produto']}\n") +
                    (f"Quantidade: {item['quantidade']}\n") +
                    (f"Preço: {item['preco']}\n") +
                    (f"Valor total em estoque: R${total_produto}\n"))
                break
        if not busca_produto:
            print("Produto não encontrado!")

#defs para alteração de dados dos produtos
def alterar_nome(produto):
    while True:
        novo_nome = input("Novo nome: ").title()
        if all(caractere.isalpha() or caractere.isspace() for caractere in novo_nome):
            produto["produto"] = novo_nome
            break
        else:
            print("Digite apenas letras")

def alterar_quantidade(produto):
    while True:
        try:
            quantidade = int(input("Nova quantidade: "))
            if quantidade < 0:
                print("Quantidade não pode ser menor que 0")
            else:
                produto["quantidade"] = quantidade
                break
        except ValueError:
            print("Digite apenas números")

def alterar_preco(produto):
    while True:
        try:
            preco = float(input("Novo preço: "))
            if preco < 0:
                print("Valor não pode ser menor que 0")
            else:
                produto["preco"] = preco
                break
        except ValueError:
            print("Digite apenas números")

def alterar_produto():
    arquivo_existe()
    cabecalho()
    with open(db,"r+", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)
        print("Qual produto deseja alterar?")
        print("0 - Cancelar")
        for indice, item in enumerate(dados):
            print(f"{indice+1} - {item['produto']}")
        alterar = int(input("Digite aqui: "))
        if alterar == 0:
            print("Operação cancelada!")
            return(menu)
        elif alterar < 1 or alterar > len(dados):
            print("Produto inexistente!")
            return
        else:
            indice = alterar
            subselecao = input(("O que deseja alterar?\n") +
                        ("1 - Alterar o nome\n") +
                        ("2 - Alterar a quantidade\n") +
                        ("3 - Alterar preço\n") + 
                        ("4 - Cancelar\n"))
            if subselecao == "1":
                alterar_nome(dados[indice])
                print("Dados alterados com sucesso")
            elif subselecao == "2":
                alterar_quantidade(dados[indice])
                print("Dados alterados com sucesso")
            elif subselecao == "3":
                alterar_preco(dados[indice])
                print("Dados alterados com sucesso")
            elif subselecao == "4":
                return
            else:
                print("Opção inválida!")

while True:
    cabecalho()
    menu()
    selecao = input("Digite a operação desejada: ")
    
    if selecao == "1":
        adicionar_produto()

    elif selecao == "2":
        listar_produto()

    elif selecao == "3":
        buscar_produto()

    elif selecao == "4":
        alterar_produto()

#    elif selecao == "5":
#       excluir_produto()
    
    elif selecao == "6":
        encerrar()
        break
    else:
        print("Opção inválida!\n")