print ("Folha de pagamento")
nome = input ("Nome: ")
salariobruto = float(input("Salário bruto: ").replace(",","."))
if(salariobruto>=3000):
    inss=(salariobruto * 0.11)
elif(salariobruto>=2000):
    inss=(salariobruto * 0.09)
else:
    inss=(salariobruto * 0.08)
if(salariobruto>=2000):
    vale = salariobruto*0.06
else:
    vale = salariobruto*0.05
if(salariobruto>=3000):
    bonus = 300
else:
    bonus = 200
if(salariobruto>=3000):
    cargo = "Acionista"
elif(salariobruto>=2000):
    cargo = "Gerente"
else:
    cargo = "Vendedor"
salarioliquido = salariobruto - (inss + vale) + bonus
print (f"Nome: {nome}")
print (f"Salário bruto: R$ {salariobruto:.2f}".replace(".",","))
print (f"INSS: R$ {inss:.2f}".replace(".",","))
print (f"Vale transporte: R$ {vale:.2f}".replace(".",","))
print (f"Bônus: R$ {bonus:.2f}".replace(".",","))
print (f"Cargo: {cargo}")
print (f"Salário Líquido: R$ {salarioliquido:.2f}".replace(".",","))