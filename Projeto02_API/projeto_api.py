#API publica de CEP: https://viacep.com.br ou https://viacep.com.br/ws/01001000/json/

import re
import requests
import json
"""
x = requests.get('https://viacep.com.br/ws/01001000/json/')
print(x.status_code)
print (x.json())
Exemplo de funcionalidade
"""
#\n pula uma linha, pode ser no começo ou final (precisa ser colocado dentro das aspas)
cep_1 = input(("Olá! Digite o CEP que deseja procurar: \n"))
cep_2 = re.sub('[^0-9]', '', cep_1)

response = requests.get(f"https://viacep.com.br/ws/{cep_2}/json/")
response_dict = response.json()

if 'erro' in response_dict:
    print("CEP inválido")
else:
    print("======RESULTADO======")
    print("CEP:", response_dict['cep'])
    print("Logradouro:", response_dict['logradouro'])
    print("Bairro:", response_dict['bairro'])
    print("Cidade:", response_dict['localidade'])
    print("Estado:", response_dict['estado'])

#print(type(response_dict))
#Isso faz com que eu vejo o tipo que está me retornando
#print(response_dict.keys())
#Esse print me mostra as chaves para chamar cada informação
#print(response_dict)

"""
print("====== RESULTADO ======")
print(f"CEP: {response_dict['cep']}")
print(f"Logradouro: {response_dict['logradouro']}")
print(f"Bairro: {response_dict['bairro']}")
print(f"Cidade: {response_dict['localidade']}")
print(f"Estado: {response_dict['estado']}")
***Aqui está uma forma mais limpa de escrever o código***
"""