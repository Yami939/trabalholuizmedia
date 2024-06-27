print ('CALCULADORA DE MEDIA')

nome_do_aluno = input('Digite o nome do aluno: ')

print(nome_do_aluno)

print('Digite as notas do aluno: ')

primeira_nota = float(input('primeira nota: '))
segunda_nota = float(input('segunda nota: '))
terceira_nota = float(input('terceira nota: '))
quarta_nota = float(input('quarta nota: '))


notas = (primeira_nota + segunda_nota + terceira_nota + quarta_nota)
media = (notas /4)

if media >= 6:
    print (nome_do_aluno,'aprovado/aprovada, nota final: ')
else:
    print (nome_do_aluno,'reprovado/reprovada, notal final: ')

print (media)


