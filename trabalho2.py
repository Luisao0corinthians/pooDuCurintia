from trabalho1 import Jogador, Equipe

jogadores = []
equipes = []

def menu():
    print("========================================")
    print("  CAMPEONATO INTERCLASSE DE E-SPORTS")
    print("========================================")
    print("1. Cadastrar jogador")
    print("2. Cadastrar equipe")
    print("3. Adicionar jogador a uma equipe")
    print("4. Listar todas as equipes")
    print("5. Listar jogadores de uma equipe")
    print("6. Buscar jogador por nickname")
    print("0. Sair")
    print("========================================")

while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome: ")
        nickname = input("Nickname: ")
        turma = input("Turma: ")

        jogador = Jogador(nome, nickname, turma)
        jogadores.append(jogador)
        print("Jogador cadastrado!")

    elif opcao == "2":
        nome = input("Nome da equipe: ")
        jogo = input("Jogo: ")

        equipe = Equipe(nome, jogo)
        equipes.append(equipe)
        print("Equipe cadastrada!")

    elif opcao == "3":
        if not jogadores or not equipes:
            print("Cadastre jogadores e equipes primeiro.")
            continue

        print("Jogadores:")
        for i, j in enumerate(jogadores):
            print(f"{i} - {j.nickname}")

        print("Equipes:")
        for i, e in enumerate(equipes):
            print(f"{i} - {e.nome}")

        try:
            i_jogador = int(input("Escolha o jogador: "))
            i_equipe = int(input("Escolha a equipe: "))

            equipes[i_equipe].adicionar_jogador(jogadores[i_jogador])
            print("Jogador adicionado!")
        except:
            print("Entrada inválida!")

    elif opcao == "4":
        for equipe in equipes:
            equipe.exibir_resumo()

    elif opcao == "5":
        for i, e in enumerate(equipes):
            print(f"{i} - {e.nome}")

        try:
            i_equipe = int(input("Escolha a equipe: "))
            equipes[i_equipe].listar_jogadores()
        except:
            print("Entrada inválida!")

    elif opcao == "6":
        nick = input("Digite o nickname: ")
        encontrado = False

        for j in jogadores:
            if j.nickname == nick:
                j.exibir_dados()
                encontrado = True

        if not encontrado:
            print("Jogador não encontrado.")

    elif opcao == "0":
        print("Encerrando...")
        break

    else:
        print("Opção inválida!")