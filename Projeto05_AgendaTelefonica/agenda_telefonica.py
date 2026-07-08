import re

# Lista para testes
'''
lista = [
     ["Matheus Lima", "11","99999-9999", "matheus@email.com"],
     ["João Silva", "11","98888-8888", "joao@email.com"],
     ["Maria Souza", "11","97777-7777", "maria@email.com"]
 ]
'''
lista = []

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
            nome2 = re.sub(r'[^a-zA-Zá-úÁ-Ú]', ' ', nome1).strip()
            #.title() metodo para a primeira letra de todas as palavras seja maiuscula e as demais minusculas
            #.capitalize() metodo para que a primeira letra seja maiuscula e as demais minusculas
            #re.sub para validar se o nome contem somente letras
            ddd1 = (input(f"Insira o DDD\n"))
            ddd2 = re.sub('[^0-9]', '', ddd1)
            #re.sub para tirar digitos que nao sejam numeros
            #ddd = re.sub('[^0-9]', '', input("Insira o DDD\n")) FORMA MAIS LIMPA DE USAR
            if len(ddd2) == 2:
                numero1 = input("Insira o numero do telefone\n")
                numero2 = re.sub('[^0-9]', '', numero1)
                #re.sub para tirar digitos que nao sejam numeros
                #numero = re.sub('[^0-9]', '', input("Insira o telefone\n")) FORMA MAIS LIMPA DE USAR
                if len(numero2) == 9 and numero2.isdigit():
                    numero_formatado = f"{numero2[0:5]}-{numero2[5:9]}"
                    email = input(f"Insira o e-mail\n").strip().lower()
                    if "@" in email and "." in email:
                        lista.append([nome2, ddd2, numero_formatado, email])
                        opcao = input("Deseja adicionar mais um contato? Sim / Não\n").strip().lower()
                        if opcao != "sim":
                            break
                    else:
                        print("E-mail inválido!")
                else:
                    print("Número inválido")
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
                      (f"Telefone: ({agenda[1]}) ") + (f"{agenda[2]}\n") + 
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
    elif selecao == "4":
        print("====Agenda====")
        remocao = input(f"Qual contato deseja apagar?\n").strip().title()
        remove_contato = False
        for agenda in lista:
            if remocao == agenda[0]:
                remove_contato = True
                lista.remove(agenda)
                print(f"Contato {remocao} removido!")
                break
        if not remove_contato: 
                print("Contato não encontrado")
    elif selecao =="5":
        print("\nEncerrando a agenda telefonica")
        break