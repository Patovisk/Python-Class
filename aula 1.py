nome = input ('digite seu nome: ')
idade = input ('digite sua idade: ')
altura = input ('digite sua altura: ')
peso = input ('digite seu peso: ')
print (nome + ' tem ' + idade + ' anos, ' + altura + ' de altura e pesa ' + peso + ' kg.')
if int(idade) >= 18:
    print ('Maior de idade')
else:
    print ('Menor de idade')