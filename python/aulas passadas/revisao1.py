qtd = int(input("Quantas notas serão utilizadas: "))
soma = 0

for nota in range (0, qtd):
    soma = soma + float(input("Digite a nota" + str(nota+1)))

media = soma / qtd
print(media)