resp = "S"
qtd = 0
soma = 0

while resp =="S":
    soma = soma + float(input("digite a nota: " + str(qtd+1)))
    qtd += 1
    resp = input("Desejo continuar? (S or N) ").upper()
    while resp != "S" and resp != "N":
        print ("opção invalida")
        resp = input("Desejo continuar? (S or N) ").upper()
media = soma/qtd
print (media)

#livro introdução a logica matematica por Edgard de Alencar Filho 
# https://www.amazon.com.br/Inicia%C3%A7%C3%A3o-L%C3%B3gica-Matem%C3%A1tica-Edgard-Alencar/dp/852130403X 
