'''print('digite os numeros ')
n1=int(input( ))
n2=int(input( ))

exp=(n1>=n2)
print(exp)

if (exp) and True:
    print('é verdadeiro')
elif(exp) and False:
     print('é falsa.')'''

nome= input('qual o seu nome ')
idade= input(' Qual sua idade')
idade=int(idade)
#Limite de idade para pegar emprestimo
ida_lmt =18

if idade >= ida_lmt:
    print(f'{ nome} pode pegar o emprestimo')
else:
    print(f'{nome} não pode pegar o emprestimo sinto muito')

 