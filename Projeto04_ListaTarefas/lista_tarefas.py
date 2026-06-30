lista = [ 'Estudar Pyhton' ,
          'Subir projetos no GitHub' ,
          'SQL'
          ]

while True:
    print("==== Lista de tarefas ====")

    selecao = input("1 - Adicionar Tarefa\n" \
                    "2 - Listar Tarefas\n" \
                    "3 - Remover Tarefa\n" \
                    "4 - Sair\n")
    
    if selecao == "1":
        while True:
            tarefa = input("Qual a tarefa que deseja adicionar?\n")
            lista.append(tarefa)
            opcao = input(f"====Deseja adicionar mais uma tarefa? Sim / Não====\n").strip().lower()
            if opcao != "sim":
                break
    elif selecao == "2":
        print("==== Lista de tarefas ====")
        if not lista:
            print("Não há tarefas cadastradas\n")
        else:
            for numeracao, tarefa in enumerate(lista, start=1):
                print(f"{numeracao} - {tarefa}")
            print("========================")
    elif selecao == "3":
        print("\n==== Lista de tarefas ====")
        if not lista:
            print("Não há tarefas cadastradas\n")
        else:
            for numeracao, tarefa in enumerate(lista, start=1):
                print(f"{numeracao} - {tarefa}")
        remocao = (int(input("\nQual tarefa deseja apagar?\n")))
        if remocao < 1 or remocao > len(lista):
            print("Tarefa inexistente")
        else:
            tarefa_removida = lista.pop(remocao - 1)
            print(f'Tarefa "{tarefa_removida}" removida com sucesso!\n')
    elif selecao == "4":
        print("\n Programa sendo encerrado")
        break
