alunos = [""] * 5 
alunos[0] = "fulano de tal"
alunos[1] = "cicrano"
for control in range(2, len(alunos)):
    alunos [control] = input("nome do aluno: ")

print("lista de alunos: ")
valor = 0
while valor < len(alunos):
    print(f"aluno {valor}: ", alunos[valor])
    valor = valor + 1