def pode_aprovar(idade, renda, valor):
    return idade > 18 and valor <= renda * 20

def definir_taxa(parcelas):
    if parcelas <= 6:
        return 0.05
    elif parcelas <= 12:
        return 0.08
    else:
        return 0.10

def calcular_parcela(valor, taxa, parcelas):
    return valor * ((taxa * (1 + taxa) ** parcelas) / ((1 + taxa) ** parcelas - 1))

def calcular_total(parcela, parcelas):
    return parcela * parcelas

def calcular_juros(total, valor):
    return total - valor


nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
renda_mensal = float(input("Digite sua renda mensal: "))
emprestimo = float(input("Digite o valor desejado do empréstimo: "))
parcelas = int(input("Digite a quantidade de parcelas (3 até 24): "))


if parcelas < 3 or parcelas > 24:
    print("Número de parcelas inválido!")
else:
    if pode_aprovar(idade, renda_mensal, emprestimo):
        taxa_juros = definir_taxa(parcelas)
        PMT = calcular_parcela(emprestimo, taxa_juros, parcelas)
        total_pago = calcular_total(PMT, parcelas)
        juros_pagos = calcular_juros(total_pago, emprestimo)

        print("\n--- Empréstimo Aprovado ---")
        print(f"Nome: {nome}")
        print(f"Valor financiado: R$ {emprestimo:.2f}")
        print(f"Taxa de juros: {taxa_juros * 100:.0f}% ao mês")
        print(f"Valor da parcela: R$ {PMT:.2f}")
        print(f"Total pago: R$ {total_pago:.2f}")
        print(f"Total de juros: R$ {juros_pagos:.2f}")
    else:
        print("\n--- Empréstimo Negado ---")