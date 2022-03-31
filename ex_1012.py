# Escreva um programa que leia três valores com ponto flutuante 
# de dupla precisão: A, B e C. Em seguida, calcule e mostre:
# a) a área do triângulo retângulo que tem A por base e C por altura.
# b) a área do círculo de raio C. (pi = 3.14159)
# c) a área do trapézio que tem A e B por bases e C por altura.
# d) a área do quadrado que tem lado B.
# e) a área do retângulo que tem lados A e B.

A,B,C = list(map(float, input().split()))

a = ((A*C)/2)
b = (3.14159)*(C**2)
c = ((A+B)*C)/2
d = (B**2)
e = (A*B)

print('TRIANGULO: %.3f'%a)
print('CIRCULO: %.3f'%b)
print('TRAPEZIO: %.3f'%c)
print('QUADRADO: %.3f'%d)
print('RETANGULO: %.3f'%e)