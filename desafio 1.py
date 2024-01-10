# esses tres programas sao tres desafios onde constituia em criar um programa que o usuario digitava seu nome e printava com uma mensagem de boas vindas, o segundo mostrava a mensagem formatada com sua data de nascimento e o terceiro em resolver um problema onde o usuario colocava dois numeros e fazia sua soma sem que o programa apenas juntasse os dois numeros como 2 + 3 = 23



nome = input('digite seu nome para iniciar o programa: ')

print('boas vindas ao nosso programa,' , nome + '!')

print('para continuar insira sua data de nascimento!')

dia = input('dia: ')
mes = input('mes: ')
ano = input('ano: ')

print('voce nasceu em', dia , 'de' , mes , 'de' , ano + '.')

print('esta sera uma tarefa simples, escreva dois numeros e realize a soma entre eles')

num1 = int(input('primeiro numero: '))
num2 = int(input('segundo numero: '))
res = num1 + num2

print('a soma entre {} e {}, vale {}' .format(num1, num2, res))

