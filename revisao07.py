#USANDO FOR, MOSTRE OS NÚMEROS PARES DE 1 A 100, mas em ordem decrescente
for i in range(100, 0, -1):
    if i % 2 == 0:
        print(i, end = " ")
