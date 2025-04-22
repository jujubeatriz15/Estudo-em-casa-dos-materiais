time1 = input("digite um time: ")
golstime1 = int(input("digite o numero de gols: "))
time2 = input("digite um time: ")
golstime2 = int(input("digite o numero de gols: "))
if golstime1 == golstime2:
    print("empate")
elif golstime1 > golstime2:
    print(f"O {time1} ganhou!")
else:
    print(f"O {time2} ganhou!")