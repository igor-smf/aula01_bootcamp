nome = input("Digite o seu nome: ")
salario = input("Digite o seu salário: ")
bonus = input("Digite o seu bonus: ")

valor_bonus = 1000 + (float(salario)*float(bonus))

print(f"Olá {nome}, o seu valor bônus foi de {valor_bonus}")