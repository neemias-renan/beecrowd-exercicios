# Calcule o consumo médio de um automóvel
# sendo fornecidos a distância total percorrida (em Km)
# e o total de combustível gasto (em litros).

distancia = int(input())
combustivelgasto = float(input())

consumomedio = distancia/combustivelgasto

print("%.3f km/l" %consumomedio)
