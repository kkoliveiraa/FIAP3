A = float(input("digite o valor do lado A: "))
B = float(input("digite o valor do lado B: "))
C = float(input("digite o valor do lado C: "))

if (A > B + C) or (B > A + C) or (C > A +B):
    print("Os valores não formam um triangulo!")
elif A == B and A == C and B == C:
    print("Triangulo Equilatero!")
elif A == B or A == C or B == C:
    print("Triangulo Isosceles!")
elif A != B and A != C and B != C:
    print("Triangulo Escaleno!")