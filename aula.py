print("poo")

nome = input("nome: ")
idade = input("idade: ")
idade = int(idade)
salario = float(input("salario: $"))

#print("Olá", nome, ". Você tem", idade, " anos.")
print(f"Olá {nome} voce tem {idade} anos.")

#print(f"Você ganha muito mal: $ {salario:.2f}")

if (salario > 10000 and salario < 15000) :
    print(f"Você ganha bem: $ {salario:.2f}")
elif(salario > 15000): 
    print("vc ganha bem p prr")
else:
    print(f"Você ganha muito mal: $ {salario:.2f}")

