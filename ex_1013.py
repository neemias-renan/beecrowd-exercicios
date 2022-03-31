# Faça um programa que leia três valores 
# e apresente o maior dos três valores lidos
# seguido da mensagem “eh o maior”. 


A,B,C = list(map(int, input().split()))

maiorAB = ((A+B+abs(A-B))/2)
maior_maiorAB_C = ((maiorAB+C+abs(maiorAB-C))/2)

print(str(int(maior_maiorAB_C))+' eh o maior')