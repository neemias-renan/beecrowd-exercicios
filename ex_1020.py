# Leia um valor inteiro correspondente à idade de uma pessoa em dias
# e informe-a em anos, meses e dias
# Obs.: apenas para facilitar o cálculo,
# considere todo ano com 365 dias e todo mês com 30 dias.
# Nos casos de teste nunca haverá uma situação que permite 12 meses
# e alguns dias, como 360, 363 ou 364.

idadeDIAS = int(input())
ano = 0
mes = 0
dia = 0

for i in range(idadeDIAS):
	if(idadeDIAS >= 365):
		ano = ano+1
		idadeDIAS = idadeDIAS-365
		
	elif(idadeDIAS >= 30 and idadeDIAS < 365):
		mes = mes+1
		idadeDIAS = idadeDIAS-30

	else:
		dia = idadeDIAS
print(str(ano)+' ano(s)')
print(str(mes)+' mes(es)')
print(str(dia)+' dia(s)')
	
	