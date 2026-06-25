
#\n pula uma linha, pode ser no começo ou final (precisa ser colocado dentro das aspas)
lista = []

while True:
    print("===== CATÁLOGO DE FILMES =====")

    selecao = input("1 - Adicionar filme\n" \
                    "2 - Listar filmes\n" \
                    "3 - Sair\n")
 
    if selecao == "1":
        while True:
            nome_filme = input(f"Qual o nome do filme?\n")
            ano = int(input("Qual o ano do filme?\n"))
            nota = float(input("Qual a nota do filme?\n"))
            lista.append([nome_filme,ano,nota])
            opcao = input(f"=====Deseja adicionar mais um filme ao catálogo? Sim / Não=====\n").strip().lower()
            if opcao != "sim":
                break

    elif selecao == "2":
        print("\n===== CATÁLOGO DE FILMES =====")
        if not lista:
            print("Não há filmes cadastrados\n")
        for filme in lista:
            print((f"{filme[0]} ") + (f"({filme[1]})"))
            print(f"Nota: {filme[2]}\n")
        opccatalogo = input("1 - Retornar ao menu anterior\n"
                            "2 - Sair\n")
        if opccatalogo == "2":
            print("\nObrigado por usar nosso catálogo, Até a próxima!\n" \
              "Sistema encerrado...")
            break

    elif selecao == "3":
        print("\nObrigado por usar nosso catálogo, Até a próxima!\n" \
              "Sistema encerrado...")
        break

    else:
        print("Opção incorreta")

"""
nome_filme
ano
nota
"""
