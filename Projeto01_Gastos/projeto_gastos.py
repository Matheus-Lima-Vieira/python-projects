'''
Gerar uma estrutura que armazene os dados:
Salario, quantidade de gastos, gastos, valores dos gastos
'''
#\n pula uma linha, pode ser no começo ou final (precisa ser colocado dentro das aspas)
salario = float(input("Olá, informe seu salário: \n"))

quant_gasto = int(input("Diga quantos gastos terá: \n"))

lista = []

gasto_total = 0

for i in range(quant_gasto):
    gasto = input("Nome do gasto: \n")
    valor = float(input("Qual o valor do gasto? \n"))
    lista.append([gasto,valor])
    gasto_total = valor + gasto_total
    
#print(gasto_total)
#print(lista)
saldo = salario - gasto_total

#Até aqui o código está funcionando perfeitamente, cria uma lista, armazena os dados e soma os valores

print("===============")
print("    RESUMO")
print("===============")

print("Salario: R${:.2f}".format(salario))
print("===============")

for item in lista:
    print(f"{item[0]}: " + "{:.2f}".format(item[1]))

    #print(f"{item[0]}: R${item[1]:.2f}")

print("===============")
print("Total de gastos: R${:.2f}".format(gasto_total))
print("Saldo restante: R${:.2f}".format(saldo))
