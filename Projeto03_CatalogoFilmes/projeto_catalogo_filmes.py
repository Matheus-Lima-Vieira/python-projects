
#\n pula uma linha, pode ser no começo ou final (precisa ser colocado dentro das aspas)
lista = []

while True:
    print("===== CATÁLOGO DE FILMES =====")

    selecao = input("1 - Adicionar filme\n" \
                    "2 - Listar filmes\n" \
                    "3 - Sair\n")

    if selecao == "1":
        opcao = input(f"=====Deseja adicionar um filme ao catálogo? Sim / Não=====\n")
        while opcao == "Sim":
            nome_filme = input(f"Qual o nome do filme?\n")
            ano = int(input("Qual o ano do filme?\n"))
            nota = input("Qual a nota do filme?\n")
            opcao = input(f"Deseja adicionar mais um filme?\n")
            lista.append([nome_filme,ano,nota])
    elif selecao == "2":
        print(lista)
        break
    elif selecao == "3":
        print("\nObrigado por usar nosso catálogo, Até a próxima!")
        print("Sistema encerrado...")
        break
    else:
        print("Opção incorreta")

"""
nome_filme
ano
nota
"""
