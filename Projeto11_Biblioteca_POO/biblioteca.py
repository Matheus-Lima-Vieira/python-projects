class Livro:
    def __init__(self,livro_id, titulo, autor, ano, disponivel=True):
        self.livro_id = livro_id
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.disponivel = disponivel

class Cliente:
    def __init__(self, cliente_id, nome):
        self.cliente_id = cliente_id
        self.nome = nome

livros = [
    Livro(1, "Harry Potter", "J. K. Rowling", 1997, True),
    Livro(2, "O Hobbit", "J. R. R. Tolkien", 1937, True),
]

clientes = [
    Cliente(1, "Matheus"), 
    Cliente(2, "Pedro")
]

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
    "Sair",
]

opcoes_usurios = [
    "Cadastrar novo usuário",
    "Listar usuários",
    "Sair",
]

# desenhar_menu("BIBLIOTECA GATO PRETO", opcoes_principal)
# desenhar_menu("BIBLIOTECA GATO PRETO", opcoes_livros)
# desenhar_menu("BIBLIOTECA GATO PRETO", opcoes_usurios)

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
                f"══════║ Titulo: {livro.titulo}\n"
                f"ID: {livro.livro_id} ║ Autor: '{livro.autor}'\n"
                f"══════║ Ano de publicação: {livro.ano}\n"
            )

def buscar_livro():
    if not livros:
        print("Nenhum livro cadastrado!")
    else:
        busca = input("Qual livro está buscando? ")
        busca_livro = False
        for livro in livros:
            if busca == livro.titulo:
                busca_livro = True
                print(
                    f"══════║ Titulo: {livro.titulo}\n"
                    f"ID: {livro.livro_id} ║ Autor: '{livro.autor}'\n"
                    f"══════║ Ano de publicação: {livro.ano}\n"
                )
                break
        if not busca_livro:
            print("Livro não encontrado :(")

def emprestar_livro():
    ()

def devolver_livro():
    ()