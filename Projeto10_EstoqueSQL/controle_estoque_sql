# conexao.commit() Salva as alterações
# conexao.close() Fecha a conexão com o bando de dados
import sqlite3


def iniciar():
    conexao = sqlite3.connect("DataBase.db")
    db = conexao.cursor()
    db.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            produto TEXT NOT NULL,
            quantidade INTEGER,
            preco FLOAT
        )
    """)
    conexao.commit()
    return conexao, db


def salvar(produto, quantidade, preco):
    db.execute(
        "INSERT INTO produtos (produto, quantidade, preco) VALUES (?, ?, ?)",
        (produto, quantidade, preco),
    )
    conexao.commit()


def menu():
    print(
        "1 - Adicionar produto\n"
        "2 - Listar produtos\n"
        "3 - Buscar produto\n"
        "4 - Alterar produto\n"
        "5 - Remover produto\n"
        "6 - Sair\n"
    )


def cabecalho():
    print("======= ESTOQUE =======")


def produto_adicionado():
    print(
        "\n================================"
        "\nProduto adicionado com sucesso!"
        "\n================================"
    )


def produto_alterado():
    print(
        "\n=============================="
        "\n Dados alterados com sucesso!"
        "\n=============================="
    )


def produto_removido(produto):
    print(
        "\n=============================="
        f"\n produto {produto} removido com sucesso!"
        "\n=============================="
    )


def encerrar():
    print("\nEncerrando o sistema")


def adicionar_produto():
    cabecalho()
    while True:
        db.execute("SELECT * FROM produtos")
        produtos = db.fetchall()
        while True:
            produto = input("Insira o produto: ").title()
            if not produto.strip():
                print("Campo obrigatório!")
                continue
            produto_existe = False
            for item in produtos:
                if produto.title() == item[1]:
                    produto_existe = True
            if produto_existe == True:
                print("Produto já cadastrado!")
                continue
            else:
                break
        while True:
            quantidade = input("Insira a quantidade: ").strip()
            if quantidade == "":
                print("Campo obrigatório!")
                continue
            try:
                quantidade = int(quantidade)
                if quantidade < 0:
                    print("Valor não pode ser menor que 0")
                else:
                    break
            except ValueError:
                print("Digite apenas números")
        while True:
            valor = input("Insira o preço: ").replace(",", ".")
            if valor == "":
                print("Campo obrigatório!")
                continue
            try:
                preco = float(valor)
                if preco < 0:
                    print("Valor não pode ser menor que 0")
                else:
                    break
            except ValueError:
                print("Digite apenas números")
        salvar(produto, quantidade, preco)
        produto_adicionado()
        opcao = input("Deseja adicionar mais um produto? S/N\n").strip().lower()
        if opcao != "s":
            break


def validar():
    db.execute("SELECT COUNT(*) FROM produtos")
    total_produtos = db.fetchone()[0]
    if total_produtos == 0:
        print("Banco de dados está vazio!")
        return False
    return True


def listar_produto():
    cabecalho()
    if not validar():
        return
    db.execute("SELECT * FROM produtos")
    produtos = db.fetchall()
    estoque_total = 0
    total_produtos = 0
    for item in produtos:
        print(f"{item[0]} - {item[1]}")
        total_produtos += 1
        valor_produtos = item[2] * item[3]
        print(f"Valor em estoque: R$ {valor_produtos:.2f}\n")
        estoque_total += valor_produtos
    print("==============================")
    print(f"TOTAL DE PRODUTOS: {total_produtos}")
    print(f"VALOR TOTAL: R${estoque_total:.2f}")
    print("==============================\n")


def buscar_produto():
    cabecalho()
    if not validar():
        return
    db.execute("SELECT * FROM produtos")
    produtos = db.fetchall()
    busca = input("Digite o produto que deseja buscar: ")
    produto_encontrado = False
    for item in produtos:
        if busca.title() == item[1]:
            produto_encontrado = True
            total_produto = item[2] * item[3]
            print(
                f"=========================\n"
                f"Produto: {item[1]}\n"
                f"Quantidade: {item[2]}\n"
                f"Preco: {item[3]:.2f}\n"
                f"Valor total em estoque: R$ {total_produto:.2f}\n"
                f"=========================\n"
            )
            break
    if produto_encontrado == False:
        print("Produto digitado não existe!\n")
        return


def alterar_produto():
    if not validar():
        return
    db.execute("SELECT * FROM produtos")
    produtos = db.fetchall()
    while True:
        cabecalho()
        print("Qual produto deseja alterar?")
        print("0 - Cancelar (Voltar para o menu inicial)")
        if len(produtos) == 0:
            print("Nenhum produto cadastrado!")
            return
        for item in produtos:
            print(f"{item[0]} - {item[1]}")
        try:
            id_produto = int(input("Digite aqui: "))
            if id_produto == 0:
                print("Operação cancelada!\n")
                return
            elif not any(item[0] == id_produto for item in produtos):
                print("Produto inexistente!\n")
                continue
            else:
                while True:
                    subselecao = input(
                        "O que deseja alterar?\n"
                        "1 - Alterar o nome\n"
                        "2 - Alterar a quantidade\n"
                        "3 - Alterar o preço\n"
                        "4 - Voltar à seleção de produtos\n"
                    )
                    if subselecao == "1":
                        alterar_nome(id_produto)
                        produto_alterado()
                        break
                    elif subselecao == "2":
                        alterar_quantidade(id_produto)
                        produto_alterado()
                        break
                    elif subselecao == "3":
                        alterar_preco(id_produto)
                        produto_alterado()
                        break
                    elif subselecao == "4":
                        break
                    else:
                        print("Opção inválida!\n")
        except ValueError:
            print("Digite apenas números!\n")


def alterar_nome(id_produto):
    while True:
        nome = input("Novo nome: ").title()
        if not nome.strip():
            print("Campo obrigatório!")
        else:
            break
    db.execute("UPDATE produtos SET produto = ? WHERE id = ?", (nome, id_produto))
    conexao.commit()


def alterar_quantidade(id_produto):
    while True:
        valor = input("Nova quantidade: ").strip()
        if not valor:
            print("Campo obrigatório!")
            continue
        try:
            quantidade = int(valor)
            if quantidade < 0:
                print("Quantidade não pode ser menor que 0!")
            else:
                break
        except ValueError:
            print("Digite apenas números!")
    db.execute(
        "UPDATE produtos SET quantidade = ? WHERE id = ?", (quantidade, id_produto)
    )
    conexao.commit()


def alterar_preco(id_produto):
    while True:
        valor = input("Novo preço: ").strip()
        if not valor:
            print("Campo obrigatório!")
            continue
        try:
            preco = float(valor)
            if preco < 0:
                print("Preço não pode ser menor que 0!")
            else:
                break
        except ValueError:
            print("Digite apenas números!")
    db.execute("UPDATE produtos SET preco = ? WHERE id = ?", (preco, id_produto))
    conexao.commit()


def excluir_produto():
    cabecalho()
    if not validar():
        return
    db.execute("SELECT * FROM produtos")
    produtos = db.fetchall()
    while True:
        print("Qual produto deseja excluir?")
        print("0 - Cancelar (Voltar para o menu inicial)")
        for item in produtos:
            print(f"{item[0]} - {item[1]}")
        try:
            id_produto = int(input("Digite aqui: "))
            if id_produto == 0:
                print("Operação cancelada!\n")
                return
            else:
                produto_nome = None
                for item in produtos:
                    if item[0] == id_produto:
                        produto_nome = item[1]
                        break
                if produto_nome is None:
                    print("Produto inexistente!\n")
                    continue
                db.execute("DELETE FROM produtos WHERE id = ?", (id_produto,))
                conexao.commit()
                produto_removido(produto_nome)
                return
        except ValueError:
            print("Digite apenas números!")


conexao, db = iniciar()
# LOOP principal ↓↓↓↓↓↓
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
        conexao.close()
        break
    # Reseta o banco de dados para testes ↓
    # elif selecao == "7":
    #     db.execute("DELETE FROM produtos")
    #     db.execute("UPDATE sqlite_sequence SET seq = 0 WHERE name = 'produtos'")
    #     conexao.commit()
    else:
        print("Opção inválida!\n")
