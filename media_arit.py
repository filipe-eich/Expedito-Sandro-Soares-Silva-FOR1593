"""
Programa: media_arit
Descrição: Este programa calcula a média aritmética entre 4 números à escolha do usuário
Autor: Filipe Eich
Data: 28/02/2025
Versao: 0.0.1
"""

#Alocaçao de memoria

a=""
c=""
b=""
d=""
m=""


#Entrada de dados

a = float(input("\nOlá! Vamos calcular a média aritmética de 4 números a, b, c, d? Comece me dizendo o valor de a: "))
b = float(input("\nAgora, me diga o valor para b: "))
c = float(input("\nAgora, me diga o valor para c: "))
d = float(input("\nPor fim, me diga o valor para d: "))


# Processamento de dados

m=(a+b+c+d)/4


#Saida de dados

print(f"\nAqui está o valor da média aritmética para os números informados: {m}")
