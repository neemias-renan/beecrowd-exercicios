# Leia um valor inteiro, que é o tempo de duração em segundos
# de um determinado evento em uma fábrica, 
# e informe-o expresso no formato horas:minutos:segundos.

tempo = int(input())

horas = 0
minutos = 0
segundos = 0

for i in range(tempo):
	if(tempo>=60):
		minutos = minutos+1
		tempo = tempo - 60
		if(minutos >= 60):
			horas = horas+1
			minutos = 0
	else:
		segundos = tempo

print(str(horas)+":"+str(minutos)+":"+str(segundos))