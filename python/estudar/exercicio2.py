# Dados
# Cps do 1 semestre
cp1 =float(input("Entre com a nota do CP1: "))
cp2 =float(input("Entre com a nota do CP2: "))
cp3 =float(input("Entre com a nota do CP3: "))

# Cps do 2 semestre
cp4 =float(input("Entre com a nota do CP4: "))
cp5 =float(input("Entre com a nota do CP5: "))
cp6 =float(input("Entre com a nota do CP6: "))

gs_s1 = float(input("Entre com a nota da GS do semestre 1: "))

gs_s2 = float(input("Entre com a nota da GS do semestre 2: "))

challenge = float(input("Entre com a nota do challenge: "))

# Processos
media_s1 = ((cp1+cp2+cp3)/3)*0.2 + challenge*0.2 + gs_s1*0.6

media_s2 = ((cp4+cp5+cp6)/3)*0.2 + challenge*0.2 + gs_s1*0.6

media_final = media_s1*0.4 + media_s2*0.6

# Saida
if media_final >= 6:
    print("Aprovado!")
elif media_final >= 4 and media_final < 6:
    print("Exame!")
elif media_final < 4:
    print("DP!")