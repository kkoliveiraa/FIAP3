#Dados
salario_bruto = float(input("Entre com o salario bruto: "))
dependente = int(input("Entre com o numero de Dependentes: "))
#Processo
if salario_bruto <= 1302:
    inss = salario_bruto*0.075
elif salario_bruto > 1302 and salario_bruto <= 2571.29:
    inss = salario_bruto*0.09
elif salario_bruto > 2571.29 and salario_bruto <= 3856.94:
    inss = salario_bruto*0.12
elif salario_bruto > 3856.94 and salario_bruto <= 7507.49:
    inss = salario_bruto*0.14
elif salario_bruto > 7507.49:
    inss = 7507.49*0.14
if salario_bruto <= 1903.98:
    print("Isento do IRPF")
    salario_base = salario_bruto - inss - (dependente * 189.59)
    print("Seu salario base é de: " + str(salario_base))
elif salario_bruto > 1903.98 and salario_bruto <= 2826.65:
    salario_base = salario_bruto - inss - (dependente * 189.59)
    imposto = salario_base*0.075 - 142.80
    salario_final = salario_base - imposto
    print("Seu salario base é de: " + str(salario_base))
    print("Seu salario final é de: " + str(salario_final))
elif salario_bruto > 2826.65 and salario_bruto <= 3751.05:
    salario_base = salario_bruto - inss - (dependente * 189.59)
    imposto = salario_base*0.15 - 354.80
    salario_final = salario_base - imposto
    print("Seu salario base é de: " + str(salario_base))
    print("Seu salario final é de: " + str(salario_final))
elif salario_bruto > 3751.05 and salario_bruto <= 4664.68:
    salario_base = salario_bruto - inss - (dependente * 189.59)
    imposto = salario_base*0.225 - 636.13
    salario_final = salario_base - imposto
    print("Seu salario base é de: " + str(salario_base))
    print("Seu salario final é de: " + str(salario_final))
elif salario_bruto > 4664.68:
    salario_base = salario_bruto - inss - (dependente * 189.59)
    imposto = salario_base*0.275 - 869.36
    salario_final = salario_base - imposto
    print("Seu salario base é de: " + str(salario_base))
    print("Seu salario final é de: " + str(salario_final))