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

    print(f"O arquivo '{DataBase}' não foi encontrado!")
    opcao = input("Deseja criar esse arquivo? (s/n): ").strip().lower()

    if opcao == "s":
        with open(DataBase, "w", encoding="utf-8") as db:
            json.dump([], db)
        print(f"Arquivo '{DataBase}' criado com sucesso")
        return True

    print("Operação cancelada. O arquivo não foi criado.")
    return False
'''
def arquivo_vazio(DataBase):
    if not os.path.exists(DataBase) or os.path.getsize(DataBase) == 0:
        return True
    try:
        with open(DataBase, "r", encoding="utf-8") as db:
            conteudo = json.load(db)
            return not bool(conteudo)
    except json.JSONDecodeError:
        return True
'''
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
    with open(db, "r+", encoding="utf-8") as arquivo:
        produtos = json.load(arquivo)
        while True:
            cabecalho()
            produto = re.sub(r'[^a-zA-Zá-úÁ-Ú]', ' ', input("Qual produto deseja adicionar?\n")).strip().title()
            quantidade = int(re.sub('[^0-9]', '', (input("Qual a quantidade desse produto?\n"))))
            preco = float(input("Qual o valor do produto? \n"))
            #lista.append([produto, quantidade, preco])
            produtos.append({"produto": produto,
                            "quantidade": quantidade,
                            "preco": preco
                            },)
            arquivo.seek(0)
            json.dump(produtos, arquivo, indent=4, ensure_ascii=False)
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
        busca = input("Qual produto deseja procurar? \n").strip().title()
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

#    elif selecao == "4":
#        alterar_produto()

#    elif selecao == "5":
#       excluir_produto()
    
    elif selecao == "6":
        encerrar()
        break
    else:
        print("Opção inválida!\n")