preco = float(input("Entre com o preco atual: "))
qtd = int(input("Entre com a quantidade: "))


if qtd < 0:
    qtd = 0
    print("Error: Quantidade negativa!")
elif preco < 0:
    preco_final = 0
    print("Error: Preço atual negativo!")


if qtd <= 500 and preco <= 30:
    preco_final = preco*1.1
elif (qtd > 500 and qtd <= 1200) and (preco > 30 and preco <= 80):
    preco_final = preco*1.15
elif qtd > 1200 and preco > 80:
    preco_final = preco*0.8
else:
    print("O preço não será alterado!")
    preco_final = preco

if preco_final < 0:
    preco_final = 0
    print("Error: Preço Final negativo!")

print("O preço final é", preco_final)