#1 - Crie um (range) numérico que apresente os números de 1 a 100;
#Range >- inicio, < fim
for numero in range (1, 101):
    print(numero)


#2 - Crie um sistema de inventario que receba um produto e aplique uma defasagem no valor
#do produto, a partir da porcentagem informada pelo usuário;

# Dados
produto = input("Entre com o nome do produto: ")
valor = float(input("Entre com o valor do produto: "))
porcentagem = float(input("Entre com o percentual de defasagem"))

# Processos
defasagem = valor*(porcentagem/100)
valor_final = valor - defasagem
# Saida
print("O valor final do produto " + str(produto) + " é de: " +str(valor_final))


#3 - Crie um sistema de atendimento de pacientes que use ifs para classificar pacientes em Urgente, Emergente e Normal,
#  tendo como base os valores de idade, pressão e oximetria;

idade = int(input("Entre com a idade"))
pressao = float(input("Entre com a pressao: "))
oximetria = float(input("Entre com a Oximetria: "))

if (idade <= 1 or idade >= 70) or (pressao < 10 or pressao > 16) or (oximetria < 90):
     print("Emergecia") 
elif ((idade > 1 and idade < 15) or (idade >= 50 and idade < 70)) or ((pressao > 10 and pressao <12) or (pressao >= 14 and pressao < 16)) or (oximetria > 90 and oximetria <= 95):
     print("Urgencia") 
else:
     print("Normal")

 #4 - Crie um sistema que calcule uma media simples a partir de 3 notas inseridas;
cp1 = float(input("Entre com a nota 1: "))
cp2 = float(input("Entre com a nota 2: "))
cp3 = float(input("Entre com a nota 3: "))

media = (cp1 + cp2 + cp3)/3

print(media)


#5 - Crie um sistema que receba as notas de 3 CPs e descarte a nota mais baixa;

cp1 = float(input("Entre com a nota 1: "))
cp2 = float(input("Entre com a nota 2: "))
cp3 = float(input("Entre com a nota 3: "))

if cp1 > cp2 and cp1 > cp3:
     nota_final_1 = cp1
     if cp2 > cp3:
          nota_final_2 = cp2
    