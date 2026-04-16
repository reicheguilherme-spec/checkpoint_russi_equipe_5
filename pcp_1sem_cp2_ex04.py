nomeFuncionario = input("Digite seu nome: ")
cargo = input("Digite seu cargo (1=Gerente, 2=Analista, 3=Assistente, 4=Estagiário): ")
salarioBase = float(input("Digite o salário: "))
totalHorasExtrasTrab = int(input("Digite o total de horas extras trabalhadas: "))
totalFaltas = int(input("Digite o total de faltas: "))
bonus = input("Recebeu bônus (s/n): ")


def valorHorasExtrasTrab(salarioBase, totalHorasExtrasTrab):
    return 0.015 * salarioBase * totalHorasExtrasTrab


def descontoPorFalta(salarioBase, totalFaltas):
    return 0.02 * salarioBase * totalFaltas


def valorBonus(cargo, salarioBase):
    if cargo == "1":
        return salarioBase + 1000
    elif cargo == "2":
        return salarioBase + 500
    elif cargo == "3":
        return salarioBase + 300
    elif cargo == "4":
        return salarioBase + 100
    else:
        return salarioBase


def salarioBruto(salarioBonus, valorExtra):
    return salarioBonus + valorExtra


def totalAcresimos(salarioBonus, salarioBase, valorExtra):
    return (salarioBonus - salarioBase) + valorExtra


def salarioFinal(salarioBruto, desconto):
    return salarioBruto - desconto

valor_extra = valorHorasExtrasTrab(salarioBase, totalHorasExtrasTrab)
desconto = descontoPorFalta(salarioBase, totalFaltas)

if bonus == "s":
    salarioBonus = valorBonus(cargo, salarioBase)
else:
    salarioBonus = salarioBase

salario_bruto = salarioBruto(salarioBonus, valor_extra)
acrescimos = totalAcresimos(salarioBonus, salarioBase, valor_extra)
salario_final = salarioFinal(salario_bruto, desconto)

print(f"O salário bruto é de R$ {salario_bruto:.2f}")
print(f"O total de acréscimos é de R$ {acrescimos:.2f}")
print(f"O total de desconto é de R$ {desconto:.2f}")
print(f"O salário final é de R$ {salario_final:.2f}")