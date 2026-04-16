cp1= float(input("Qual a nota do Checkpoint 1?: "))
cp2 = float(input("Qual a nota do Checkpoint 2?: "))
cp3 = float(input("Qual a nota do Checkpoint 3?: "))
sp1 = float(input("Qual a nota da Sprint 1?: "))
sp2 = float(input("Qual a nota da Sprint 2?: "))
gs = float(input("Qual a nota da Global Solution?: "))

menor = 0

if cp1 < cp2 and cp1 < cp3:
    menor = cp1
elif cp2 < cp1 and cp2 < cp3:
    menor = cp2
else:
    menor = cp3

media = ((cp1 + cp2 + cp3 - menor + sp1 + sp2) / 4) * 0.4 + gs * 0.6
mediaPeso = media * 0.4

print(f"\nEssa é sua média do semestre sem peso!: {media:.1f}")
print(f"Essa é sua média do semestre com peso!: {mediaPeso:.1f}")

