from pathlib import Path
#   "r" = modo padrão de leitura (o arquivo precisa existir)
#   "w" = modo de escrita (apaga o conteudo anterior ou cria um novo arquivo)
#   "a" = modo de anexar (adiciona novos textos no final do arquivo)
#   "x" = modo para criar um novo arquivo caso ele não exista
#   "b" = modo binário, usado para aruivos binários, como imagens ou vídeos
#   "t" = modo de texto para arquivos de texto
#   arquivo.readline(): Le um linha por vez
#   arquivo.readlines(): Le todas as linhas e transforma o conteudo em uma lista de strings

#Define o nome do arquivo
db = "DataBase.txt"
DataBase = Path(db)

#Vericar se o arquivo existe
if DataBase.is_file():
    print(f"Arquivo '{db}' encontrado!")
else:
    print(f"O arquivo '{db}' não foi encontrado!")
    #Pergunta se o usuário quer criar o arquivo
    opcao = input("Deseja criar esse arquivo? (s/n): ").strip().lower()
    if opcao == "s":
        DataBase.touch()
        print(f"Arquivo '{db}' criado com sucesso")
    else:
        print("Operação cancelada. O arquivo não foi criado.")

#Abre o arquivo e lê linha por linha
with open("DataBase.txt", "r") as db:
    linha = db.readline()
    while linha:
        print(linha.strip().split(";"))
        linha = db.readline()


















#open("Testetxt", "r")
'''
with open("Testetxt", "r") as db:
    linha = db.readline()
    while linha:
        print(linha.strip().split(";"))
        linha = db.readline()

with open("Testetxt", "a") as db:
        db.write("Monitor")
        db.write("50")
        db.write("200.99")
        db.write("\n")
'''