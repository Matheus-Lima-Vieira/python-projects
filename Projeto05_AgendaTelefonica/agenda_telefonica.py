import re

# Lista para testes
lista = [
     ["Matheus Lima", "11","99999-9999", "matheus@email.com"],
     ["João Silva", "11","98888-8888", "joao@email.com"],
     ["Maria Souza", "11","97777-7777", "maria@email.com"]
 ]

#lista = []

while True:
    print("====Agenda====")
    
    selecao = input("1 - Adicionar Contato\n" \
                    "2 - Listar Contatos\n" \
                    "3 - Buscar contato\n" \
                    "4 - Remover Contato\n"
                    "5 - Sair\n")
    if selecao == "1":
        while True:
            print("====Agenda====")
            nome1 = input(f"Insira o nome do contato\n").strip().title()
            nome2 = re.sub(r'[^a-zA-Zá-úÁ-Ú]', ' ', nome1)
            #.title() metodo para a primeira letra de todas as palavras seja maiuscula e as demais minusculas
            #.capitalize() metodo para que a primeira letra seja maiuscula e as demais minusculas
            #re.sub para validar se o nome contem somente letras
            ddd1 = (input(f"Insira o DDD\n"))
            ddd2 = re.sub('[^0-9]', '', ddd1)
            #re.sub para tirar digitos que nao sejam numeros
            if len(ddd2) == 2:
                #ddd_formatado = ddd
                numero1 = input("Insira o numero do telefone\n")
                numero2 = re.sub('[^0-9]', '', numero1)
                #re.sub para tirar digitos que nao sejam numeros
                email = input(f"Insira o e-mail\n")
                lista.append([nome2, ddd2, numero2, email])
                opcao = input("Deseja adicionar mais um contato? Sim / Não\n").strip().lower()
                if opcao != "sim":
                    break
            else:
                print("DDD está incorreto")
    elif selecao == "2":
        print("====Agenda====")
        if not lista:
            print("Nenhum contato cadastrado\n")
        else:
            for agenda in lista:
                #print(lista)
                print((f"Nome: {agenda[0]}\n") + 
                      (f"Telefone: ({agenda[1]})") + (f"{agenda[2]}\n") + 
                      (f"E-mail: {agenda[3]}\n"))
    elif selecao == "3":
        print("====Agenda====")
        busca = input(f"Qual o nome do contato que deseja buscar?\n").strip().title()
        busca_contato = False
        for agenda in lista:
            if busca == agenda[0]:
                busca_contato = True
                print((f"\nContato encontrado!\n") + 
                    (f"Nome: {agenda[0]}\n") + 
                    (f"Telefone: ({agenda[1]})") + (f"{agenda[2]}\n") + 
                    (f"E-mail: {agenda[3]}\n"))
                break
        if not busca_contato: 
                print("Contato não encontrado")
#===================================================================================================
    elif selecao == "4":
        print("====Agenda====")
        remocao = input(f"Qual contato deseja apagar?\n")
        remove_contato = False
        for agenda in lista:
            if remocao == agenda[0]:
                remove_contato = True
                #contato_removido = lista.remove(lista[0])
                print(f"Contato {remocao} removido!\n")
                break
        if not remove_contato: 
                print("Contato não encontrado")
#===================================================================================================
    elif selecao =="5":
        print("\nEncerrando a agenda telefonica")
        break