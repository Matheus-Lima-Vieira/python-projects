import re
'''
1 - Adicionar produto
2 - Listar produtos
3 - Buscar produto
4 - Atualizar quantidade
5 - Remover produto
6 - Sair
'''
#Lista para testes

lista = [
    ["Mouse", 10, 89.90],
    ["Teclado", 5, 199.90],
    ["Monitor", 3, 899.90]
]

#lista = []
while True:
    print("==== ESTOQUE ====")
    selecao = input("1 - Adicionar produto\n" \
                    "2 - Listar produtos\n" \
                    "3 - Buscar produto\n" \
                    "4 - Atualizar quantidade\n" \
                    "5 - Remover produto\n" \
                    "6 - Sair\n")
    if selecao == "1":
        print("==== ESTOQUE ====")
        produto = re.sub(r'[^a-zA-Zá-úÁ-Ú', '', input("Qual produto deseja adicionar?\n")).strip().title()
        quantidade = re.sub('[^0-9]', '', int(input("Qual a quantidade desse produto?\n")))
        preco = re.sub('[^0-9]', '', float(input("Qual o valor do produto?\n")))
        opcao = input("Deseja adicionar mais um produto? Sim / Não\n").strip().lower()
        if opcao != "sim":
            break
    elif selecao =="2":
        print("==== ESTOQUE ====")