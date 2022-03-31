# Neste problema, deve-se ler o código de uma peça 1,
# o número de peças 1, o valor unitário de cada peça 1,
# o código de uma peça 2, o número de peças 2 e o valor unitário
# de cada peça 2. Após, calcule e mostre o valor a ser pago.

codigo1, numero1 , valorUnitario1 = list(map(float, input().split()))
codigo2, numero2 , valorUnitario2 = list(map(float, input().split()))

valortotal1 = numero1*valorUnitario1
valortotal2 = numero2*valorUnitario2

valorfinal = valortotal1+valortotal2
print("VALOR A PAGAR: R$ %.2f"%valorfinal)