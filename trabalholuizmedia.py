print ('CALCULADORA DE MEDIA')

print('Digite as notas do aluno: ')

primeira_nota = float(input('primeira nota: '))
segunda_nota = float(input('segunda nota: '))
terceira_nota = float(input('terceira nota: '))
quarta_nota = float(input('quarta nota: '))

notas = (primeira_nota + segunda_nota + terceira_nota + quarta_nota)
media = (notas /4)

if media >= 6:
    print ('Aluno aprovado, nota final:')
else:
    print ('Aluno reprovado, nota final:')


print (media)


