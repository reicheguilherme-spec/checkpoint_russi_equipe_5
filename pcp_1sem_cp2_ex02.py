a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))

if a < b:
    a, b = b, a

if a < c:
    a, c = c, a

if b < c:
    b, c = c, b

print(f"A = {a}, B = {b}, C = {c}")

if a >= b + c:
    print("NAO FORMA TRIANGULO")

else:
    if a**2 == b**2 + c**2:
        print("TRIANGULO RETANGULO")

    elif a**2 > b**2 + c**2:
        print("TRIANGULO OBTUSANGULO")

    else:
        print("TRIANGULO ACUTANGULO")

    if a == b and b == c:
        print("TRIANGULO EQUILATERO")

    elif a == b or b == c or c == a:
        print("TRIANGULO ISOSCELES")