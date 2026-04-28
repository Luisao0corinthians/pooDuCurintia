class Jogador:
    def __init__(self, nome, nickname, turma):
        self.nome = nome
        self.nickname = nickname
        self.turma = turma

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Nickname: {self.nickname}")
        print(f"Turma: {self.turma}")


class Equipe:
    def __init__(self, nome, jogo):
        self.nome = nome
        self.jogo = jogo
        self.jogadores = []  # lista de objetos Jogador

    def adicionar_jogador(self, jogador):
        self.jogadores.append(jogador)

    def listar_jogadores(self):
        if not self.jogadores:
            print("Nenhum jogador na equipe.")
            return

        for jogador in self.jogadores:
            print("------------------")
            jogador.exibir_dados()

    def exibir_resumo(self):
        print(f"Equipe: {self.nome} | Jogo: {self.jogo}")
        print(f"Quantidade de jogadores: {len(self.jogadores)}")