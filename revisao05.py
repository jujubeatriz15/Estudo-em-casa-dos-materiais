#Faça um algoritmo que leia o valor do salário mínimo e o valor do salário de um usuário, calcule quantos
#salários mínimos esse usuário ganha e imprima na tela o resultado. (Base para o Salário mínimo R$ 1.412,00).
salariomin = 1412
salario_usuario = int(input("Digite aqui o seu salário: "))

div = salario_usuario // salariomin
print(div)
