# Leia um valor inteiro. 
# A seguir, calcule o menor número de notas possíveis (cédulas)
# no qual o valor pode ser decomposto. 
# As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1.
#A seguir mostre o valor lido e a relação de notas necessárias.

valor = int(input())
valorcopia = valor
n100 = 0
n50 = 0
n20 = 0
n10 = 0
n5 = 0
n2 = 0
n1 = 0

for i in range(valor):
	if(valor >= 100):
		valor = valor-100
		n100 = n100+1
	elif(valor >= 50 and valor < 100):
		valor = valor-50
		n50 = n50+1
	elif(valor >= 20 and valor < 50):
		valor = valor-20
		n20 = n20+1
	elif(valor >= 10 and valor < 20):
		valor = valor-10
		n10 = n10+1
	elif(valor >= 5 and valor < 10):
		valor = valor-5
		n5 = n5+1
	elif(valor >= 2 and valor < 5):
		valor = valor-2
		n2 = n2+1
	elif(valor >= 1 and valor < 2):
		valor = valor-1
		n1 = n1+1
	else:
		break
print(valorcopia)
print(str(n100) +" nota(s) de R$ 100,00")
print(str(n50) +" nota(s) de R$ 50,00")
print(str(n20) +" nota(s) de R$ 20,00")
print(str(n10) +" nota(s) de R$ 10,00")
print(str(n5) +" nota(s) de R$ 5,00")
print(str(n2) +" nota(s) de R$ 2,00")
print(str(n1)+" nota(s) de R$ 1,00")
