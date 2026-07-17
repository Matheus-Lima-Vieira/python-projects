import re

#Lista para testes
lista = [
    ["Mouse", 10, 89.90,],
    ["Teclado", 5, 199.90],
    ["Monitor", 3, 899.90]
]

#lista = []
while True:
    print("==== ESTOQUE ====")
    selecao = input("1 - Adicionar produto\n" \
                    "2 - Listar produtos\n" \
                    "3 - Buscar produto\n" \
                    "4 - Alterar produto\n" \
                    "5 - Remover produto\n" \
                    "6 - Sair\n")
    if selecao == "1":
        while True:
            print("==== ESTOQUE ====")
            produto = re.sub(r'[^a-zA-Zá-úÁ-Ú]', ' ', input("Qual produto deseja adicionar?\n")).strip().title()
            quantidade = int(re.sub('[^0-9]', '', (input("Qual a quantidade desse produto?\n"))))
            #preco = float(re.sub('[^0-9]', '', (input("Qual o valor do produto?\n"))))
            preco = float(input("Qual o valor do produto? \n"))
            lista.append([produto, quantidade, preco])
            opcao = input("Deseja adicionar mais um produto? Sim / Não\n").strip().lower()
            if opcao != "sim":
                break
#==================================================================
    elif selecao == "2":
        print("==== ESTOQUE ====")
        if not lista:
            print("Nenhum produto cadastrado")
        else:
            valor_total = 0
            for estoque in lista:
                valor_item = estoque[1] * estoque[2]
                print((f"Item: {estoque[0]}\n") +
                      (f"Quantidade: {estoque[1]:.0f} \n") +
                      (f"Preço R$: {estoque[2]:.2f}\n") +
                      (f"Valor total em estoque: R${valor_item:.2f}\n"))
                valor_total += valor_item
        
        print(f"\nValor total do estoque R$:{valor_total:.2f}\n")
#==================================================================
    elif selecao == "3":
        print("==== ESTOQUE ====")
        busca = input("Qual produto deseja procurar? \n").strip().title()
        busca_produto = False
        for produto in lista:
            if busca == produto[0]:
                busca_produto = True
                valor_item = produto[1] * produto[2]
                print(("\nProduto encontrado! \n") +
                     (f"Produto: {produto[0]}\n") +
                     (f"Quantidade: {produto[1]:.0f}\n") +
                     (f"Preço: {produto[2]:.2f}\n") +
                     (f"Valor total em estoque: R${valor_item:.2f}\n"))
                break
        if not busca_produto:
            print("Produto não encontrado!")
#==================================================================
    elif selecao == "4":
        print("==== ESTOQUE ====")
        print("Qual produto deseja alterar?")
        for produto in lista:
            print(f"Nome: {produto[0]}")
        alterar = input("Digite aqui: ").strip().title()
        busca_produto = False
        for produto in lista:
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
#==================================================================
    elif selecao == "5":
                print("==== ESTOQUE ====")
                print("Qual produto deseja excluir?")
                for produto in lista:
                    print(f"Nome: {produto[0]}")
                excluir = input("Digite aqui: ").strip().title()
                busca_produto = False
                for produto in lista:
                    if excluir == produto[0]:
                        busca_produto = True
                        lista.remove(produto)
                        print(f"Item ({excluir}) removido do estoque!\n")
                        break
                if not busca_produto:
                    print("Produto não encontrado!")
#==================================================================
    elif selecao =="6":
        print("\nEncerrando o sistema")
        break