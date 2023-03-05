#O IBGE (instituto Brasileiro de Geografia e Estisticas) 
# para definir um preço médio de um produto alimentar,por exemplo: 
# feijão pega o preçco em 5 mercados de tamanhos variados. 
# Após ler os valores dos 5 mercados  , calcular o preço medio e exibir !

print('Olá, vamos participar da pesquisa de preços médio ')
print('digite o nome do produto')
nome=str(input( ))

print('digite o primeiro preço')
P1=float(input( ))
print('digite o segundo preço')
P2=float(input( ))
print('digite o terçeiro preço')
P3=float(input( ))
print('digite o quarto preço')
P4=float(input( ))
print('falta pouco, digite o quinto valor ')
P5=float(input( ))
P_m=(P1+P2+P3+P4+P5)/5
print("O preço médio do ",nome,"é de R$" ,P_m)
