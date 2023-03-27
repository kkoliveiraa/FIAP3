mediaPrimeiroSem = float(input("digite a media do primeiro semestre: "))
mediaSegundoSem =  float(input("digite a media do segundo semestre: "))

mediaFinal = (mediaPrimeiroSem + mediaSegundoSem) / 2

if mediaFinal >= 0 and mediaFinal < 4:
    print("reprovado")
elif mediaFinal >= 4 and mediaFinal < 6:
    print("exame")
elif mediaFinal >= 6 and mediaFinal <= 10:
    print("aprovado")
else:
    print("valor invalido")