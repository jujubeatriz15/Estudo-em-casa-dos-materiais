repetir = "s" or "S"

while repetir == "s" or repetir == "S":
    num = int(input("digite um numero: "))
    if num > 0:
        if num % 2:
            print("par e positivo")
        else:
            print("impar e positivo")
    else:
        if num % 2 == 0:
            print("par e negativo")
        else:
            print("impar e negativo")

    repeticao = input("digite s ou S para continuar: ")
    print("fim")