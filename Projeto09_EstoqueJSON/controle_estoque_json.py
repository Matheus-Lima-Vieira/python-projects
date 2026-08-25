#json.load() para ler o arquivo
#json.dump() para gravar o arquivo
import json
from pathlib import Path

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
        with open(DataBase, "w", encoding="utf-8") as db_file:
            json.dump([], db_file)
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

def salvar_arquivo(dados):
    with open(db, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)

def encerrar():
    print("\nEncerrando o sistema")

def adicionar_produto():
    if not arquivo_existe():
        return
    #Abre o arquivo Json
    with open(db, "r", encoding="utf-8") as arquivo:
        try:
            dados = json.load(arquivo)
        except json.JSONDecodeError:
            print("O arquivo JSON está vazio ou inválido.")
            return
        #Loop do adicionar produto
        while True:
            cabecalho()
            #Loop para pedir o produto
            while True:
                produto = input("Qual produto deseja adicionar?\n").title()
                #Valida se o nome está vazio
                if not produto.strip():
                    print("É necessário preencher o nome!")
                    continue
                #Valida se o produto já existe
                produto_existe = False
                for item in dados:
                    if produto.title() == (item['produto']):
                        produto_existe = True
                if produto_existe == True:
                    print("Produto já cadastrado!")
                    continue
                else:
                # Removido o isalpha() para aceitar números e símbolos (ex: PS5, Cabo USB-C)
                    break
                    
            #Loop para pedir a quantidade
            while True:
                #Valida se foi digitando um int
                quantidade = (input("Qual a quantidade desse produto?\n")).strip()
                if quantidade == "":
                    print("É necessário preencher a quantidade!")
                    continue
                try:
                    quantidade = int(quantidade)
                    if quantidade < 0:
                        print("Valor não pode ser menor que 0")
                    else:
                        break
                except ValueError:
                    print("Digite apenas números")
                    
            #Loop para pedir o valor
            while True:
                #Valida se foi digitado um valor float (e troca vírgula por ponto)
                valor = (input("Qual o valor do produto? \n")).replace(',', '.')
                if valor == "":
                    print("É necessário preencher o preço!")
                    continue
                try:
                    preco = float(valor)
                    if preco < 0:
                        print("Valor não pode ser menor que 0")
                    else:
                        break
                except ValueError:
                    print("Digite apenas números")
                    
            dados.append({"produto": produto,
                            "quantidade": quantidade,
                            "preco": preco
                            })
            salvar_arquivo(dados)
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
        try:
            dados = json.load(arquivo)
        except json.JSONDecodeError:
            print("O arquivo JSON está vazio ou inválido.")
            return
            
        if not dados:
            print("Nenhum produto cadastrado!")
        for indice, item in enumerate(dados):
            print(f"{indice+1} - {item['produto']}"
                f"\nQuantidade: {item['quantidade']}"
                f"\nPreço: R$ {item['preco']:.2f}")
            
            total_produtos += 1
            valor_produtos = (item["quantidade"]) * (item["preco"])
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
        try:
            dados = json.load(arquivo)
        except json.JSONDecodeError:
            print("O arquivo JSON está vazio ou inválido.")
            return
            
        busca = input("Qual produto deseja procurar? \n").title()
        busca_produto = False
        for item in dados:
            if busca.strip().title() == item["produto"]:
                busca_produto = True
                total_produto = int(item["quantidade"]) * float(item["preco"])
                print(("\nProduto encontrado!\n") +
                    (f"Produto: {item['produto']}\n") +
                    (f"Quantidade: {item['quantidade']}\n") +
                    (f"Preço: {item['preco']:.2f}\n") +
                    (f"Valor total em estoque: R${total_produto:.2f}\n"))
                break
        if not busca_produto:
            print("Produto não encontrado!")

#defs para alteração de dados dos produtos
def alterar_nome(produto):
    while True:
        novo_nome = input("Novo nome: ").title()
        if not novo_nome.strip():
            print("É necessário preencher o nome!")
        else:
            produto["produto"] = novo_nome
            break

def alterar_quantidade(produto):
    while True:
        valor = input("Nova quantidade: ").strip()
        if not valor:
            print("É necessário preencher a quantidade!")
            continue
        try:
            quantidade = int(valor)
            if quantidade < 0:
                print("Quantidade não pode ser menor que 0")
            else:
                produto["quantidade"] = quantidade
                break
        except ValueError:
            print("Digite apenas números")

def alterar_preco(produto):
    while True:
        valor = input("Novo preço: ").replace(',', '.')
        if not valor:
            print("É necessário preencher o preço!")
            continue
        try:
            preco = float(valor)
            if preco < 0:
                print("Valor não pode ser menor que 0")
            else:
                produto["preco"] = preco
                break
        except ValueError:
            print("Digite apenas números")

def alterar_produto():
    if not arquivo_existe():
        return
    
    with open(db,"r", encoding="utf-8") as arquivo:
        try:
            dados = json.load(arquivo)
        except json.JSONDecodeError:
            print("O arquivo JSON está vazio ou inválido.")
            return
            
        while True: # <--- NOVO LOOP PRINCIPAL DE ALTERAÇÃO
            cabecalho()
            print("Qual produto deseja alterar?")
            print("0 - Cancelar (Voltar ao menu inicial)")
            
            if len(dados) == 0:
                print("Nenhum produto cadastrado!")
                return
                
            for indice, item in enumerate(dados):
                print(f"{indice+1} - {item['produto']}")
            
            try:
                alterar = int(input("Digite aqui: "))
                if alterar == 0:
                    print("Operação cancelada!\n")
                    return # Volta para o menu inicial
                elif alterar < 1 or alterar > len(dados):
                    print("Produto inexistente!\n")
                    continue # Volta para a pergunta de qual produto alterar
                else:
                    indice = alterar - 1
                    
                    while True: # <--- NOVO LOOP DO SUBMENU
                        subselecao = input(("O que deseja alterar?\n") +
                                    ("1 - Alterar o nome\n") +
                                    ("2 - Alterar a quantidade\n") +
                                    ("3 - Alterar preço\n") + 
                                    ("4 - Voltar à seleção de produtos\n"))
                        
                        if subselecao == "1":
                            alterar_nome(dados[indice])
                            salvar_arquivo(dados)
                            print("Dados alterados com sucesso\n")
                            break # Volta para selecionar os produtos
                        elif subselecao == "2":
                            alterar_quantidade(dados[indice])
                            salvar_arquivo(dados)
                            print("Dados alterados com sucesso\n")
                            break
                        elif subselecao == "3":
                            alterar_preco(dados[indice])
                            salvar_arquivo(dados)
                            print("Dados alterados com sucesso\n")
                            break
                        elif subselecao == "4":
                            break # Sai do submenu e volta para selecionar os produtos
                        else:
                            print("Opção inválida!\n")
            except ValueError:
                print("Digite apenas números!\n")

def excluir_produto():
    if not arquivo_existe():
        return
        
    with open(db, "r", encoding="utf-8") as arquivo:
        try:
            dados = json.load(arquivo)
        except json.JSONDecodeError:
            print("O arquivo JSON está vazio ou inválido.")
            return
            
        while True: # <--- NOVO LOOP PARA EXCLUSÃO
            cabecalho()
            print("Qual produto deseja excluir?")
            print("0 - Cancelar (Voltar ao menu inicial)")
            
            if len(dados) == 0:
                print("Nenhum produto cadastrado.")
                return
                
            for indice, item in enumerate(dados):
                print(f"{indice+1} - {item['produto']}")
                
            try:
                excluir = int(input("Digite aqui: "))
                if excluir == 0:
                    print("Operação cancelada!\n")
                    return # Volta para o menu inicial
                elif excluir < 1 or excluir > len(dados):
                    print("Opção inválida!\n")
                    continue # Volta para tentar escolher outro número
                else:
                    indice = excluir - 1
                    produto_removido = dados.pop(indice)
                    salvar_arquivo(dados)
                    print(f"Produto '{produto_removido['produto']}' removido com sucesso!\n")
                    # O código continuará rodando o laço 'while' permitindo 
                    # que você exclua outro, se não quiser, é só digitar '0' e ele retorna.
            except ValueError:
                print("Digite apenas números!\n")

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