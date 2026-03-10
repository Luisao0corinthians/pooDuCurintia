import os
comandoEmail = "git config user.email \"20241pvai00310012@estudantes.ifpr.edu.br\""
comando1 = "git add *"

mensagem = input("mensagem do commit: ")
while(len(mensagem) < 5):
    print("mensagem muito pequena, digite mais. . .")
    mensagem = input("mensagem do commit: ")

comando2 = f"git commit -m \"{mensagem}\" "
comando3 = "git push"

print(". . . configurando email")
os.system(comandoEmail)

print(". . . adicionando notificações")
os.system(comando1)

print(". . . realizando commit")
os.system(comando2)

print(". . . fazendo o push")
os.system(comando3)