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
    with open(db, "a", encoding="utf-8") as arquivo:
        while True:
            cabecalho()
            produto = re.sub(r'[^a-zA-Zá-úÁ-Ú]', ' ', input("Qual produto deseja adicionar?\n")).strip().title()
            quantidade = int(re.sub('[^0-9]', '', (input("Qual a quantidade desse produto?\n"))))
            #preco = float(re.sub('[^0-9]', '', (input("Qual o valor do produto?\n"))))
            preco = float(input("Qual o valor do produto? \n"))
            #lista.append([produto, quantidade, preco])
            arquivo.write(f"{produto};{quantidade};{preco:.2f}\n")
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
    print("==============================")
    with open(db, "r", encoding="utf-8") as arquivo:
        for indice, linha in enumerate(arquivo):
            produto = linha.strip().split(";")
            if linha.strip():
                print(f"{indice+1} - {produto[0]}\n" +
                    f"Quantidade: {produto[1]}\n" +
                    f"preço: R${produto[2]}")
                total_produtos += 1
                valor_produtos = int(produto[1]) * float(produto[2])
                print(f"Valor em estoque: R${valor_produtos:.2f}\n")
                estoque_total += valor_produtos
    print("==============================")
    print(f"TOTAL DE PRODUTOS: {total_produtos}")
    print(f"VALOR TOTAL: R${estoque_total:.2f}")
    print("==============================")

def buscar_produto():
    arquivoexiste()
    cabecalho()
    with open(db, "r", encoding="utf-8") as arquivo:
        busca = input("Qual produto deseja procurar? \n").strip().title()
        busca_produto = False
        for linha in arquivo:
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

def alterar_nome(produto):
    produto[0] = input("Novo nome: ").title()

# Primeira utilização de try/except para validar entradas do usuário.
def alterar_quantidade(produto):
    while True:
        try:
            quantidade = int(input("Nova quantidade: "))
            produto[1] = str(quantidade)
            break
        except ValueError:
            print("Digite apenas números.")

def alterar_preco(produto):
    while True:
        try:
            preco = float(input("Novo preço: "))
            produto[2] = f"{preco:.2f}"
            break
        except ValueError:
            print("Digite um valor válido.")

def alterar_produto():
    arquivoexiste()
    cabecalho()
    with open(db, "r", encoding="utf-8") as arquivo:
            print("Qual produto deseja alterar?")
            print("0 - Cancelar")
            linhas = arquivo.readlines()
            for indice, linha in enumerate(linhas):
                produto = linha.strip().split(";")
                print(f"{indice+1} - {produto[0]}")
            alterar = int(input("Digite aqui: "))
            if alterar == 0:
                print("Operação cancelada!")
                return(menu)
            elif alterar > len(linhas):
                print("Produto inexistente!")
                return
            else:
                #print("Item encontrado!")
                indice = alterar -1
                #Novo Submenu
                subselecao = input(("O que deseja alterar?\n") +
                            ("1 - Alterar o nome\n") +
                            ("2 - Alterar a quantidade\n") +
                            ("3 - Alterar preço\n") + 
                            ("4 - Cancelar\n"))
                
                produto = linhas[indice].strip().split(";")
                if subselecao == "1":
                    alterar_nome(produto)
                    print("Dados alterados com sucesso")
                elif subselecao == "2":
                    alterar_quantidade(produto)
                    print("Dados alterados com sucesso")
                elif subselecao == "3":
                    alterar_preco(produto)
                    print("Dados alterados com sucesso")
                elif subselecao == "4":
                    return
                else:
                    print("Opção inválida!")
                linhas[indice] = ";".join(produto) + "\n"
                with open(db, "w", encoding="utf-8") as arquivo:
                    arquivo.writelines(linhas)

def excluir_produto():
    arquivoexiste()
    cabecalho()
    with open(db, "r", encoding="utf-8") as arquivo:
        print("Qual produto deseja excluir?")
        print("0 - Cancelar")
        linhas = arquivo.readlines()
        for indice, linha in enumerate(linhas):
            produto = linha.strip().split(";")
            print(f"{indice+1} - {produto[0]}")
        excluir = int(input("Digite aqui: "))
        if excluir == 0:
            print("Operação cancelada!")
            return(menu)
        elif excluir > len(linhas):
            print("Opção inválida!\n")
            return
        else:
            indice = excluir - 1
            produto_removido = linhas.pop(indice)
            removido = produto_removido.split(";")[0]
        with open(db, "w", encoding="utf-8") as arquivo:
            arquivo.writelines(linhas)
            print(f"Produto '{removido}' excluido com sucesso!")
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

    elif selecao == "5":
       excluir_produto()
    
    elif selecao == "6":
        encerrar()
        break
    else:
        print("Opção inválida!\n")