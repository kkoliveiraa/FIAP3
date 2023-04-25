id = [1, 2]
produtos = ["Banana", "Notebook"]
qtd = [20, 2]
validade = [3, -1]
lote = [12345, 54321]
valor_compra = [1.0, 3500.0]
valor_atual = [1.0, 3000.0]
data_entrada = ["18/03/2023", "01/01/2023"]
data_saida = ["", ""]
departamento = ["Copa", "RH"]
filial = ["São Paulo", "São Paulo"]

def adicionar():
    id[len()-1]+1
    id.append([len(id)-1]+1)
    produtos.append(input("Entre com o produto: ".title()))
    qtd.append(int(input("Entre com a quantidade: ")))
    validade.append(int(input("Entre com a validade: ")))
    lote.append(int(input("Entre com o lote do produto: ")))
    preco = float(input("Entre com o preço produto: "))
    valor_compra.append(preco)
    valor_atual.append(preco)
    data_entrada.append(input("Entre com a data de entrada do produto: "))
    data_saida.append("")
    departamento.append(input("Entre com o departamento: "))
    filial.append(input("Entre com o nome da filial: "))

def alterar_preco():
    altera = input("Entre com o nome do produto: ").title()
    if altera in produtos:
        for index in range(0, len(id)):
            if altera == produtos[index]:
                new_preco = float(input("Entre com o novo preço: "))
                valor_atual[index] = new_preco
                print("\nID:....................", id[index])
                print("Nome:..................", produtos[index])
                print("Quantidade:............", qtd[index])
                if validade[index] < 0:
                    tempo = "Produto sem validade definida"
                else:
                    tempo = str(validade[index])
                print("Validade:..............", tempo)
                print("Lote:..................", lote[index])
                print("Valor Atual:...........", valor_atual[index])
                print("Valor de compra:.......", valor_compra[index])
                print("Valor total alocado:...", (int(valor_compra[index])*int(qtd[index])))
                print("Data de entrada:.......", data_entrada[index])
                if data_saida[index] == "":
                    tmp = "Produto não vendido!"
                else:
                    tmp = data_saida[index]
                print("Data de saida:.........", tmp)
                print("Departamento:..........",departamento[index])
                print("Filial:................", filial[index])

def busca():
    busca = input("entre com o produto: ")
    for elemento in range(0, len(produtos)):
        if busca == produtos[elemento]:
            print("Achei")
            produtos[elemento] = input("entre com o produto: ")
def adicionar():
    produtos.append(input("entre com o produto: "))
def remover():
    produtos.remove(input("entre com o produto a remover: "))
    #del produtos[0]

def vender():
    ...

alterar_preco()