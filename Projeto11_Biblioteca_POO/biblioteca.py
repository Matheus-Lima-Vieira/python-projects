class Livro:
    def __init__(self,livro_id, titulo, autor, ano, disponivel=True):
        self.livro_id = livro_id
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.disponivel = disponivel

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            print("Livro emprestado com sucesso!")
        else:
            print("Livro já está emprestado.")

    def devolver(self):
        if not self.disponivel:
            self.disponivel = True
            print("Livro devolvido com sucesso!")
        else:
            print("Livro já está disponível.")

class Cliente:
    def __init__(self, cliente_id, nome, rg):
        self.cliente_id = cliente_id
        self.nome = nome
        self.rg = rg

livros = [
    Livro(1, "Harry Potter", "J. K. Rowling", 1997, True),
    Livro(2, "O Hobbit", "J. R. R. Tolkien", 1937, True),
]

clientes = [
    Cliente(1, "Matheus", 508175604), 
    Cliente(2, "Pedro", 508175605)
]

titulo_biblioteca = "BIBLIOTECA GATO PRETO"
def desenhar_menu(titulo_biblioteca, opcoes):
    tamanho = 40  # Largura da caixa

    print(f"╔{'═' * tamanho}╗")
    # Centraliza o título dentro do tamanho estipulado
    print(f"║{titulo_biblioteca.center(tamanho)}║")
    print(f"╠{'═' * tamanho}╣")

    for i, opcao in enumerate(opcoes, 1):
        texto = f" {i} - {opcao}"
        # Alinha à esquerda e preenche com espaço até bater na borda direita
        print(f"║{texto.ljust(tamanho)}║")

    print(f"╚{'═' * tamanho}╝")

# Para usar, basta passar uma lista:
opcoes_principal = [
    "Livros",
    "Usuários",
    "Sair",
]

opcoes_livros = [
    "Cadastrar novo livro",
    "Listar livros",
    "Emprestar livro",
    "Devolver livro",
    "Buscar livro",
    "Voltar ao menu anterior",
]

opcoes_usurios = [
    "Cadastrar novo usuário",
    "Listar usuários",
    "Voltar ao menu anterior",
]

def cadastrar_livro():
    tamanho = 40

    print(f"╔{'═' * tamanho}╗")
    print(f"║{'CADASTRAR NOVO LIVRO'.center(tamanho)}║")
    print(f"╠{'═' * tamanho}╣")
    ##############################################################
    titulo = input("║ Título: ")
    autor = input("║ Autor: ")
    ano = input("║ Ano: ")
    ##############################################################
    print(f"╚{'═' * tamanho}╝")
    ##############################################################
    novo_livro = Livro(len(livros)+1,titulo, autor, int(ano), True)
    livros.append(novo_livro)
    ##############################################################
    print(f"╔{'═' * tamanho}╗")
    print(f"║{'LIVRO CADASTRADO COM SUCESSO!'.center(tamanho)}║")
    print(f"╚{'═' * tamanho}╝")

def listar_livros():
    if not livros:
        print("Nenhum livro cadastrado!")
    else:
        for livro in livros:
            print(
                f"╔══════║ Titulo: {livro.titulo}\n"
                f"║ID: {livro.livro_id} ║ Autor: '{livro.autor}'\n"
                f"╚══════║ Ano de publicação: {livro.ano}\n"
            )

def buscar_livro():
    if not livros:
        print("Nenhum livro cadastrado!")
    else:
        busca = input("Qual livro está buscando?\n")
        busca_livro = False
        for livro in livros:
            if busca == livro.titulo:
                busca_livro = True
                print(
                    f"╔══════║ Titulo: {livro.titulo}\n"
                    f"║ID: {livro.livro_id} ║ Autor: '{livro.autor}'\n"
                    f"╚══════║ Ano de publicação: {livro.ano}\n"
                )
                break
        if not busca_livro:
            print("Livro não encontrado :(")

def emprestar_livro():
    if not livros:
        print("Nenhum livro cadastrado!")
    else:
        titulo_buscado = input("Qual livro deseja pegar emprestado?\n")
        livro_encontrado = False

        for livro in livros:
            if titulo_buscado == livro.titulo:
                livro_encontrado = True
                livro.emprestar()
                break

        if not livro_encontrado:
            print("Livro não encontrado no sistema.")
        

def devolver_livro():
    if not livros:
        print("Nenhum livro cadastrado!")
    else:
        titulo_buscado = input("Qual livro está devolvendo?\n")
        livro_encontrado = False

        for livro in livros:
            if titulo_buscado == livro.titulo:
                livro_encontrado = True
                livro.devolver()
                break

        if not livro_encontrado:
            print("Livro não encontrado no sistema.")

def cadastrar_cliente():
    tamanho = 40

    print(f"╔{'═' * tamanho}╗")
    print(f"║{'CADASTRAR NOVO CLIENTE'.center(tamanho)}║")
    print(f"╠{'═' * tamanho}╣")
    ##############################################################
    nome = input("║ Nome: ")
    rg = input("║ RG: ")
    ##############################################################
    print(f"╚{'═' * tamanho}╝")
    ##############################################################
    novo_cliente = Cliente(len(clientes) + 1, nome, int(rg))
    clientes.append(novo_cliente)
    ##############################################################
    print(f"╔{'═' * tamanho}╗")
    print(f"║{'CLIENTE CADASTRADO COM SUCESSO!'.center(tamanho)}║")
    print(f"╚{'═' * tamanho}╝")


def listar_clientes():
    tamanho = 40

    if not clientes:
        print("Nenhum livro cadastrado!")
    else:
        print(f"╔{'═' * tamanho}╗")
        print(f"║{'CLIENTES'.center(tamanho)}║")
        print(f"╠{'═' * tamanho}╝")
        for cliente in clientes:
            print(f"║ID: {cliente.cliente_id}")
            print(f"║Nome: {cliente.nome}")
            print(f"║RG: {cliente.rg}")
            print(f"╚{'═' * tamanho}╝")

def encerrar():    
    tamanho = 40

    print(f"╔{'═' * tamanho}╗")
    print(f"║{titulo_biblioteca.center(tamanho)}║")
    print(f"╠{'═' * tamanho}╣")
    texto = "Obrigado por usar nosso sistema!"
    print(f"║{texto.center(tamanho)}║")
    print(f"╚{'═' * tamanho}╝")

# #=============================================================================#
while True:
    desenhar_menu(titulo_biblioteca, opcoes_principal)
    opcao = input("Digite a opção desejada: ")
    if opcao == "1":
        while True:
            desenhar_menu(titulo_biblioteca, opcoes_livros)
            opcao = input("Digite a opção desejada: ")
            if opcao == "1":
                cadastrar_livro()
            elif opcao == "2":
                listar_livros()
            elif opcao == "3":
                emprestar_livro()
            elif opcao == "4":
                devolver_livro()
            elif opcao == "5":
                buscar_livro()
            elif opcao == "6":
                break
    elif opcao == "2":
        while True:
            desenhar_menu(titulo_biblioteca, opcoes_usurios)
            opcao = input("Digite a opção desejada: ")
            if opcao == "1":
                cadastrar_cliente()
            elif opcao == "2":
                listar_clientes()
            elif opcao == "3":
                break
    elif opcao =="3":
        encerrar()
        break
    else:
        print("Opção inválida!")