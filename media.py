#Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, 
# imprima o número de alunos com média maior ou igual a 7.0.

import os
media = 0.0
notas = list()
medias = list()
numAlunos = 0
try:
  for x in range(1,11):
      print(f'''Digite as Notas do {x}ª Aluno''')
      for y in range(1,5):  
        notas.append(float(input(f'''Digite a {y}ª nota ''')))
        os.system('cls') or None         
      media = (notas[0]+notas[1]+notas[2]+notas[3])/4
      medias.append(media)
      notas.clear()
      if(media >= 7):
        numAlunos += 1
except ValueError:
    print("O tipo de dado de entrada é inválido")    
    
print(f'''Quantidade de alunos Com média >= 7 são: {numAlunos}''')
