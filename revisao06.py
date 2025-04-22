altura = float(input("Digite sua altura: "))
peso = float(input("Digite sua peso: "))
imc = peso / altura ** 2

if imc < 18.6:
    print("Abaixo do peso")
elif imc >= 25.0 or imc <= 29.9:
    print("Levemente acima do peso")
elif imc >= 30.0 or imc <= 34.9:
    print("Obesidade grau I")
elif imc >= 35.0 or imc <=  39.9:
    print("Obesidade grau II (severa)")
else:
    print("Obesidade grau III (mórbida")
