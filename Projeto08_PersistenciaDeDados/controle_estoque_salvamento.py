#   "r" = modo padrão de leitura (o arquivo precisa existir)
#   "w" = modo de escrita (apaga o conteudo anterior ou cria um novo arquivo)
#   "a" = modo de anexar (adiciona novos textos no final do arquivo)
#   "x" = modo para criar um novo arquivo caso ele não exista
#   "b" = modo binário, usado para aruivos binários, como imagens ou vídeos
#   "t" = modo de texto para arquivos de texto
#   arquivo.readline(): Le um linha por vez
#   arquivo.readlines(): Le todas as linhas e transforma o conteudo em uma lista de strings
import re
from pathlib import Path

selecao = ()
db = "DataBase.txt"
DataBase = Path(db)

#Abre o arquivo e lê linha por linha
#Teste para visualizar a lista
'''
with open("DataBase.txt", "r", encoding="utf-8") as db:
    linha = db.readline()
    while linha:
        print(linha.strip().split(";"))
        linha = db.readline()
'''
#=============================================================
def arquivoexiste():
    #Vericar se o arquivo existe
    if DataBase.is_file():
        print(f"Arquivo '{DataBase}' encontrado!\n")
    else:
        print(f"O arquivo '{DataBase}' não foi encontrado!")
        #Pergunta se o usuário quer criar o arquivo
        opcao = input("Deseja criar esse arquivo? (s/n): ").strip().lower()
        if opcao == "s":
            DataBase.touch()
            print(f"Arquivo '{DataBase}' criado com sucesso")
        else:
            print("Operação cancelada. O arquivo não foi criado.")

def menu(): 
    print("1 - Adicionar produto\n" \
        "2 - Listar produtos\n" \
        "3 - Buscar produto\n" \
        "4 - Alterar produto\n" \
        "5 - Remover produto\n" \
        "6 - Sair\n")

def cabecalho():
    print("==== ESTOQUE ====")

def encerrar():
    print("\nEncerrando o sistema")

def adicionar_produto():
    with open("DataBase.txt", "a") as db:
        while True:
            cabecalho()
            produto = re.sub(r'[^a-zA-Zá-úÁ-Ú]', ' ', input("Qual produto deseja adicionar?\n")).strip().title()
            quantidade = int(re.sub('[^0-9]', '', (input("Qual a quantidade desse produto?\n"))))
            #preco = float(re.sub('[^0-9]', '', (input("Qual o valor do produto?\n"))))
            preco = float(input("Qual o valor do produto? \n"))
            #lista.append([produto, quantidade, preco])
            db.write(f"{produto};{quantidade};{preco:.2f}\n")
            print("Produto adicionado com sucesso!\n")
            opcao = input("Deseja adicionar mais um produto? S/N\n").strip().lower()
            if opcao != "s":
                break

def listar_produto():
    #valor total de estoque
    estoque_total = 0
    #valor total de cada produto
    total_produtos = 0
    arquivoexiste()
    cabecalho()
    with open("DataBase.txt", "r", encoding="utf-8") as db:
        for linha in db:
            produto = linha.strip().split(";")
            if linha.strip():
                print(f"Produto: {produto[0]}\n" +
                      f"Quantidade: {produto[1]}\n" +
                      f"Valor: R${produto[2]}")
                total_produtos += 1
                valor_produtos = int(produto[1]) * float(produto[2])
                print(f"Valor total do produto em estoque: R${valor_produtos:.2f}\n")
                estoque_total += valor_produtos
    print(f"Valor total do estoque: R${estoque_total:.2f}")
    print(f"Total de itens encontrados: {total_produtos}\n")

def buscar_produto():
    arquivoexiste()
    cabecalho()
    with open("DataBase.txt", "r", encoding="utf-8") as db:
        busca = input("Qual produto deseja procurar? \n").strip().title()
        busca_produto = False
        for linha in db:
            produto = linha.strip().split(";")
            if busca == produto[0]:
                busca_produto = True
                total_produto = int(produto[1]) * float(produto[2])
                print(("\nProduto encontrado!\n") +
                    (f"Produto: {produto[0]}\n") +
                    (f"Quantidade: {produto[1]}\n") +
                    (f"Preço: {produto[2]}\n") +
                    (f"Valor total em estoque: R${total_produto}\n"))
                break
        if not busca_produto:
            print("Produto não encontrado!")

def alterar_produto():
    cabecalho()
    with open("DataBase.txt", "r", encoding="utf-8") as db:
        print("Qual produto deseja alterar?")
        busca_produto = False
        for linha in db:
            produto = linha.strip().split(";")
            print(f"Produto: {produto[0]}")
        '''alterar = input("Digite aqui: ").strip().title()
        #for produto in db:
        if alterar == produto[0]:
            busca_produto = True
            print("Item encontrado!")
            #Novo submenu
            subselecao = input(("O que deseja alterar?\n") +
                        ("1 - Alterar o nome\n") +
                        ("2 - Alterar a quantidade\n") +
                        ("3 - Alterar preço\n"))
            if subselecao == "1":
                produto[0] = input("Qual o novo nome do produto?\n").strip().title()
                print("Dados alterados com sucesso")
            elif subselecao == "2":
                produto[1] = int(input("Qual a nova quantidade do produto?\n"))
                print("Dados alterados com sucesso")
            elif subselecao == "3":
                produto[2] = float(input("Qual o novo valor do produto?\n"))
                print("Dados alterados com sucesso")
            else:
                print("Opção inválida!")
    if not busca_produto:
        print("Nenhum produto encontrado!")'''

#============================================================================================
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

    #elif selecao == "5":
    #   excluir_produto()
    
    elif selecao == "6":
        encerrar()
        break