salario = float(input("Entre com o Salario: "))

print("Para Analista Jr digite 1")
print("Para Analista Pleno digite 2")
print("Para Analista Senior digite 3")
print("Para Arquiteto digite 4")
print("Para Gerente digite 5")
cargo = int(input("Entre com a opção de cargo: "))

ajuste = float(input("Entre com o percentual de ajuste: "))
porcento = ajuste/100

if cargo == 1:
    salario_final = salario*(1 + porcento) + salario*0.02
elif cargo == 2:
    salario_final = salario(1 + porcento) + salario*0.025
elif cargo == 3:
    salario_final = salario(1 + porcento) + salario*0.03
elif cargo == 4:
    salario_final = salario(1 + porcento) + salario*0.04
elif cargo == 5:
    salario_final = salario(1 + porcento) + salario*0.045

print("O Salario final sera de", salario_final)