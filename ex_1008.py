# Escreva um programa que leia o número de um funcionário,
# seu número de horas trabalhadas,
# o valor que recebe por hora e 
# calcula o salário desse funcionário. 
# A seguir, mostre o número e o salário do funcionário,
# com duas casas decimais.

numero = int(input())
hrs_trabalhadas = int(input())
valor_hora = float(input())

salario = float(hrs_trabalhadas*valor_hora)

print("NUMBER = "+str(numero))
print("SALARY = U$ %.2f" %salario)

