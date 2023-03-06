# Uma loja de tintas deseja informar aos seu clintes: 
# o melhor custo-benefício na compra de suas tintas .
# O programa deve ser desenvolvido para que não tenha desperdicio 
# sabendo que 1 Lt cobre 6m² 
# e as embalagens vendidas são em:
# latas de 18 Lt que custam R$80,00
# galões de 3,6 lt que custam R$25,00
# devemos devemos dar 3 respostas:
# (A)comprar apenas latas de 18 litros  
# (B) comprar apenas galoes 
# (C) misturar lats e galões , pois o desperdício sera menor 
#' obs. ( Acrescentar 10% de folga e sempre arredondar os valores para cima ,isto é ,
 #considerar lts cheias )

print('Olá, seja bem vindo A Super loja das Tintas')
print('digite seu nome ')
nome= str(input( ))

print('vamos começar ,Sr', nome,' digite a altura de sua parede, use ponto em vez de virgula ok ,ok' ), 
al=float(input( ))
print('A gora digite a largura de sua parede Sr(a)',nome,) 
lrg=float(input( ))

m_q=al*lrg 
print('O m² de sua parede é de ' , m_q , 'm²')

print('A norma das boas praticas diz que precisa de acrescentar 10% de tinta ')
#bap= boa pratica
bap=m_q/10
print('acrescente mais 10% a medida que é', bap, 'm²')
#Tt_mq=(é o m² + 10%)
Tt_mq=m_q+bap
print('o valor total é', Tt_mq, 'm²')

lata=(Tt_mq//108)
lata1=(lata*108)
print(f'Precisa Compra>>>> {lata} lata de 18 lt')
print(lata1)
 
# 1 lt (um litro ) pinta 6m²
galão=(Tt_mq-lata1)/21.6
c_galao= (galão+0.99)//1

print(f'Comprar apenas >>>>{c_galao} galões de 3.6 lts')
#qt_G= quantidade de galões
qt_G=(galão / 3.6)

#if Tt_mq <= 107:
# print(f'comprar apenas{qt_G}')
#elif qt_G >= 108:
# print('comprar lata {lata}')
#print('quantidade de galão é', qt_G)
#print('''[a1] compre so latas de 18 lts;
#[b1compre apenas galões de 3,6 lts;
#[c1] compre galões e lts de 18 litros]''')

     
