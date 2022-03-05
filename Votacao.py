import os
candidatos = ["Ricardo","Neusa","Simone"]
total_votos = 0
votados = [0,0,0]
print("Candidatos: \n--> Ricardo: 13\n--> Neusa: 04\n--> Simone: 25")
voto = int(input("se quiser iniciar a votação digite 1: "))

if(voto == 1):
     os.system('cls') or None
     while voto != 0:
         print("Candidatos: \n--> Ricardo: 13\n--> Neusa: 04\n--> Simone: 25")
         voto = int(input("Digite o Número do Candidato que Deseja Votar: "))
         if voto == 13:
             votados[0] += 1
             total_votos += 1
             os.system('cls') or None
         elif voto == 4:
            votados[1] += 1
            total_votos +=1
            os.system('cls') or None
         elif voto == 25:
             votados[2] += 1
             total_votos += 1
             os.system('cls') or None
             
         elif voto == 0:
            os.system('cls') or None
            break
          
     
por_primeiro = (100*votados[0]/total_votos)  
por_segundo = (100*votados[1]/total_votos)
por_terceiro = (100*votados[2]/total_votos)

print("O candidato ",candidatos[0]," possui ",por_primeiro,"% ","dos votos")
print("O candidato ",candidatos[1]," possui ",por_segundo,"% ","dos votos")
print("O candidato ",candidatos[2]," possui ",por_terceiro,"% ","dos votos") 

           
