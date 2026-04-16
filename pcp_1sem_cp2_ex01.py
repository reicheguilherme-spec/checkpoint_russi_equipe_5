estado = int(input("Digite o código do estado de origem (1 a 5): "))
peso = float(input("Digite o peso da carga (em toneladas): "))
codigo_carga = int(input("Digite o código da carga (10 a 40): "))

if 10 <= codigo_carga <= 20:
    preco = 100

elif 21 <= codigo_carga <= 30:
    preco = 250

elif 31 <= codigo_carga <=40:
    preco = 340

else:
    preco = 0

if estado==1:
    taxa_imposto = 0.35

elif estado==2:
    taxa_imposto = 0.25

elif estado ==3:
    taxa_imposto = 0.15

elif estado==4:
    taxa_imposto = 0.05

else:
    taxa_imposto = 0

kg = peso * 1000
preco_carga = kg * preco
imposto = preco_carga * taxa_imposto
total = preco_carga + imposto


print(f"O peso da carga do caminhão convertido em quilos é de:", kg, "kg")
print(f"O Preço da carga é de: R$ {preco_carga:.2f}")
print(f"Imposto ({taxa_imposto*100}%): R$ {imposto:.2f}")
print(f"Total transportado: R$ {total:.2f}")