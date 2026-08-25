import arcade
import random

LARGURA = 800
ALTURA = 600
TITULO = "Coletor de Tesouros"

VELOCIDADE_JOGADOR = 4
QUANTIDADE_MOEDAS = 25
PONTOS_MOEDA_ESPECIAL = 5
PONTUACAO_MAXIMA = QUANTIDADE_MOEDAS + PONTOS_MOEDA_ESPECIAL


def desenhar_texto_central(texto, altura, tamanho=18, cor=arcade.color.WHITE):
    arcade.draw_text(
        texto,
        LARGURA / 2,
        altura,
        cor,
        tamanho,
        anchor_x="center",
    )


class Jogador(arcade.Sprite):
    def __init__(self):
        super().__init__("direita.png", scale=0.17)

        self.textura_direita = arcade.load_texture("direita.png")
        self.textura_esquerda = arcade.load_texture("esquerda.png")

    def update(self, delta_time=1 / 60):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.change_x > 0:
            self.texture = self.textura_direita
        elif self.change_x < 0:
            self.texture = self.textura_esquerda

        if self.left < 0:
            self.left = 0

        if self.right > LARGURA:
            self.right = LARGURA

        if self.bottom < 0:
            self.bottom = 0

        if self.top > ALTURA:
            self.top = ALTURA


class Moeda(arcade.Sprite):
    def __init__(self):
        super().__init__("moeda.png", scale=0.1)


class MoedaEspecial(arcade.Sprite):
    def __init__(self):
        super().__init__("moeda.png", scale=0.14)

    def update(self, delta_time=1 / 60):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0:
            self.left = 0
            self.change_x *= -1

        elif self.right > LARGURA:
            self.right = LARGURA
            self.change_x *= -1

        if self.bottom < 0:
            self.bottom = 0
            self.change_y *= -1

        elif self.top > ALTURA:
            self.top = ALTURA
            self.change_y *= -1


class Inimigo(arcade.Sprite):
    def __init__(self):
        super().__init__("inimigo.png", scale=0.09)

    def update(self, delta_time=1 / 60):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0:
            self.left = 0
            self.change_x *= -1

        elif self.right > LARGURA:
            self.right = LARGURA
            self.change_x *= -1

        if self.bottom < 0:
            self.bottom = 0
            self.change_y *= -1

        elif self.top > ALTURA:
            self.top = ALTURA
            self.change_y *= -1


class InimigoEspecial(arcade.Sprite):
    def __init__(self, jogador):
        super().__init__("goblin.png", scale=0.12)

        self.jogador = jogador
        self.velocidade = 1.5

    def update(self, delta_time=1 / 60):

        if self.center_x < self.jogador.center_x:
            self.center_x += self.velocidade

        elif self.center_x > self.jogador.center_x:
            self.center_x -= self.velocidade

        if self.center_y < self.jogador.center_y:
            self.center_y += self.velocidade

        elif self.center_y > self.jogador.center_y:
            self.center_y -= self.velocidade


class TelaMenu(arcade.View):

    def on_show_view(self):
        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        self.clear()

        desenhar_texto_central(
            "COLETOR DE TESOUROS",
            430,
            32,
            arcade.color.YELLOW
        )

        opcoes = [
            "[J] Jogar",
            "[I] Instruções",
            "[S] Sobre o jogo",
            "[ESC] Sair",
        ]

        altura = 330

        for opcao in opcoes:
            desenhar_texto_central(opcao, altura)
            altura -= 45

    def on_key_press(self, key, modifiers):

        if key == arcade.key.J:
            self.window.show_view(TelaJogo())

        elif key == arcade.key.I:
            self.window.show_view(TelaInstrucoes())

        elif key == arcade.key.S:
            self.window.show_view(TelaSobre())

        elif key == arcade.key.ESCAPE:
            arcade.close_window()


class TelaInstrucoes(arcade.View):

    def on_show_view(self):
        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        self.clear()

        desenhar_texto_central(
            "INSTRUÇÕES",
            530,
            30
        )

        instrucoes = [
            "Colete todas as moedas para terminar o jogo.",
            "Cada moeda normal vale 1 ponto.",
            "A moeda especial rebate nas paredes e vale 5 pontos.",
            "O inimigo comum rebate nas paredes e tira 1 ponto.",
            "O goblin persegue o jogador.",
            "Depois da colisão, o goblin teletransporta.",
            "Movimentação: teclas WASD ou setas direcionais.",
        ]

        altura = 455

        for texto in instrucoes:
            arcade.draw_text(
                texto,
                70,
                altura,
                arcade.color.WHITE,
                16
            )

            altura -= 43

        desenhar_texto_central(
            "[M] ou [ESC] Voltar ao menu",
            100,
            16,
            arcade.color.LIGHT_GRAY
        )

    def on_key_press(self, key, modifiers):

        if key == arcade.key.M or key == arcade.key.ESCAPE:
            self.window.show_view(TelaMenu())


class TelaSobre(arcade.View):

    def __init__(self):
        super().__init__()

        self.lista_avatares = arcade.SpriteList()

        self.avatar = arcade.Sprite(
            "direita.png",
            scale=0.08
        )

        self.avatar.center_x = LARGURA / 2
        self.avatar.center_y = 270

        self.lista_avatares.append(self.avatar)

    def on_show_view(self):
        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        self.clear()

        desenhar_texto_central(
            "SOBRE O JOGO",
            500,
            30
        )

        desenhar_texto_central(
            "Desenvolvido por:",
            420
        )

        desenhar_texto_central(
            "Luís Rafael Cargnin de Oliveira - 3º Info",
            375,
            20,
            arcade.color.YELLOW
        )

        self.lista_avatares.draw()

        desenhar_texto_central(
            "[M] ou [ESC] Voltar ao menu",
            100,
            16,
            arcade.color.LIGHT_GRAY
        )

    def on_key_press(self, key, modifiers):

        if key == arcade.key.M or key == arcade.key.ESCAPE:
            self.window.show_view(TelaMenu())


class TelaJogo(arcade.View):

    def __init__(self):
        super().__init__()

        self.pontos = 0
        self.tempo = 0.0

        self.alerta_dano = False
        self.tempo_alerta = 0.0

        self.tempo_sem_novo_dano = 0.0

        self.lista_jogador = arcade.SpriteList()
        self.lista_moedas = arcade.SpriteList()
        self.lista_inimigos = arcade.SpriteList()
        self.lista_inimigo_especial = arcade.SpriteList()

        # Jogador
        self.jogador = Jogador()

        self.jogador.center_x = LARGURA / 2
        self.jogador.center_y = ALTURA / 2

        self.lista_jogador.append(self.jogador)

        # Moedas normais
        for i in range(QUANTIDADE_MOEDAS):

            moeda = Moeda()

            self.posicionar_sem_colisao(
                moeda,
                self.lista_moedas
            )

            self.lista_moedas.append(moeda)

        # Moeda especial
        self.moeda_especial = MoedaEspecial()

        self.posicionar_sem_colisao(
            self.moeda_especial,
            self.lista_moedas
        )

        self.moeda_especial.change_x = 3
        self.moeda_especial.change_y = 3

        self.lista_moedas.append(self.moeda_especial)

        # Inimigo comum
        self.inimigo = Inimigo()

        self.posicionar_sem_colisao(
            self.inimigo,
            self.lista_moedas
        )

        self.inimigo.change_x = 2
        self.inimigo.change_y = 2

        self.lista_inimigos.append(self.inimigo)

        # Goblin - inimigo especial
        self.inimigo_especial = InimigoEspecial(
            self.jogador
        )

        self.posicionar_sem_colisao(
            self.inimigo_especial,
            self.lista_moedas
        )

        self.lista_inimigo_especial.append(
            self.inimigo_especial
        )

    def on_show_view(self):
        arcade.set_background_color(
            arcade.color.AMAZON
        )

    def posicionar_sem_colisao(
        self,
        sprite,
        lista_existente
    ):
        """
        Sorteia uma posição sem colocar
        o objeto sobre o jogador ou outra moeda.
        """

        for tentativa in range(100):

            sprite.center_x = random.randint(
                50,
                LARGURA - 50
            )

            sprite.center_y = random.randint(
                50,
                ALTURA - 50
            )

            colidiu_jogador = arcade.check_for_collision(
                sprite,
                self.jogador
            )

            colidiu_lista = arcade.check_for_collision_with_list(
                sprite,
                lista_existente
            )

            if not colidiu_jogador and len(colidiu_lista) == 0:
                return

    def ativar_alerta(self):

        self.alerta_dano = True
        self.tempo_alerta = 0.7

    def on_draw(self):

        self.clear()

        self.lista_moedas.draw()
        self.lista_inimigos.draw()
        self.lista_inimigo_especial.draw()
        self.lista_jogador.draw()

        arcade.draw_text(
            f"Pontos: {self.pontos}",
            15,
            570,
            arcade.color.WHITE,
            16
        )

        arcade.draw_text(
            f"Tempo: {self.tempo:.1f} segundos",
            15,
            545,
            arcade.color.WHITE,
            14
        )

        if self.alerta_dano:

            desenhar_texto_central(
                "DANO RECEBIDO! -1 PONTO",
                510,
                20,
                arcade.color.RED
            )

    def on_update(self, delta_time):

        self.tempo += delta_time

        self.lista_jogador.update()
        self.lista_moedas.update()
        self.lista_inimigos.update()
        self.lista_inimigo_especial.update()

        # Tempo do alerta
        if self.tempo_alerta > 0:

            self.tempo_alerta -= delta_time

            if self.tempo_alerta <= 0:
                self.alerta_dano = False

        # Tempo entre danos
        if self.tempo_sem_novo_dano > 0:

            self.tempo_sem_novo_dano -= delta_time

        # Verificar moedas coletadas
        moedas_coletadas = arcade.check_for_collision_with_list(
            self.jogador,
            self.lista_moedas
        )

        for moeda in moedas_coletadas:

            if isinstance(moeda, MoedaEspecial):
                self.pontos += PONTOS_MOEDA_ESPECIAL

            else:
                self.pontos += 1

            moeda.remove_from_sprite_lists()

        # Inimigo comum
        inimigos_atingidos = arcade.check_for_collision_with_list(
            self.jogador,
            self.lista_inimigos
        )

        if len(inimigos_atingidos) > 0:

            if self.tempo_sem_novo_dano <= 0:

                self.pontos -= 1

                self.tempo_sem_novo_dano = 1.0

                self.ativar_alerta()

        # Goblin
        inimigo_especial_atingido = arcade.check_for_collision_with_list(
            self.jogador,
            self.lista_inimigo_especial
        )

        if len(inimigo_especial_atingido) > 0:

            self.pontos -= 1

            self.ativar_alerta()

            # Teletransporta o goblin
            self.posicionar_sem_colisao(
                self.inimigo_especial,
                self.lista_moedas
            )

        # Terminou o jogo
        if len(self.lista_moedas) == 0:

            tela_final = TelaGameOver(
                self.pontos,
                self.tempo
            )

            self.window.show_view(tela_final)

    def on_key_press(self, key, modifiers):

        if key == arcade.key.UP or key == arcade.key.W:
            self.jogador.change_y = VELOCIDADE_JOGADOR

        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.jogador.change_y = -VELOCIDADE_JOGADOR

        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.jogador.change_x = -VELOCIDADE_JOGADOR

        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.jogador.change_x = VELOCIDADE_JOGADOR

        elif key == arcade.key.ESCAPE:
            self.window.show_view(TelaMenu())

    def on_key_release(self, key, modifiers):

        if key in [
            arcade.key.UP,
            arcade.key.DOWN,
            arcade.key.W,
            arcade.key.S
        ]:

            self.jogador.change_y = 0

        if key in [
            arcade.key.LEFT,
            arcade.key.RIGHT,
            arcade.key.A,
            arcade.key.D
        ]:

            self.jogador.change_x = 0


class TelaGameOver(arcade.View):

    def __init__(self, pontos, tempo):

        super().__init__()

        self.pontos = pontos
        self.tempo = tempo

    def on_show_view(self):

        arcade.set_background_color(
            arcade.color.AMAZON
        )

    def on_draw(self):

        self.clear()

        if self.pontos == PONTUACAO_MAXIMA:

            desenhar_texto_central(
                "VITÓRIA PERFEITA!",
                430,
                32,
                arcade.color.GOLD
            )

            desenhar_texto_central(
                "Você escapou de todos os inimigos perfeitamente!",
                375,
                18
            )

        else:

            desenhar_texto_central(
                "PARABÉNS! JOGO CONCLUÍDO",
                430,
                28,
                arcade.color.YELLOW
            )

        desenhar_texto_central(
            f"Pontuação final: {self.pontos}",
            300,
            20
        )

        desenhar_texto_central(
            f"Tempo total: {self.tempo:.1f} segundos",
            260,
            18
        )

        desenhar_texto_central(
            "[M] Voltar ao menu   |   [ESC] Sair",
            160,
            16,
            arcade.color.LIGHT_GRAY
        )

    def on_key_press(self, key, modifiers):

        if key == arcade.key.M:

            self.window.show_view(
                TelaMenu()
            )

        elif key == arcade.key.ESCAPE:

            arcade.close_window()


def main():

    janela = arcade.Window(
        LARGURA,
        ALTURA,
        TITULO
    )

    janela.show_view(
        TelaMenu()
    )

    arcade.run()


if __name__ == "__main__":
    main()
