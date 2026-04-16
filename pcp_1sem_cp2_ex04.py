nomeFuncionario = input("Digite seu nome: ")
cargo = input("Digite seu cargo (1=Gerente, 2=Analista, 3=Assistente, 4=Estagiário): ")
salarioBase = float(input("Digite o sálario: "))
totalHorasExtrasTrab = input("Digite o total de horas extras trabalhadas: ")
totalFaltas = input("Digite o total de faltas: ")
bonus = input("Recebeu bônus (s/n): ")

print(nomeFuncionario)
print("Salário é R$" f"{salarioBase:.2f}")
print("O total de horas trabalhadas é de" f"{totalHorasExtrasTrab}")
print("O número total de faltas é" f"{totalFaltas}")
if bonus == "s":
    print("Ele recebeu bônus")
else:
    print("Ele não recebeu bônus")
if cargo == "1":
    print("O cargo é Gerente")
if cargo == "2":
    print("O cargo é Analista")
if cargo == "3":
    print("O cargo é Assistente")
if cargo == "4":
    print("O cargo é Estagiário")
