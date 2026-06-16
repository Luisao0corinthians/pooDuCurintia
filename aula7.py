import arcade
import random


class Jogador(arcade.Sprite):
    def __init__(self):
        super().__init__("direita.png", scale=0.2)

        self.textura_direita = arcade.load_texture("direita.png")
        self.textura_esquerda = arcade.load_texture("esquerda.png")

    def update(self, delta_time):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.change_x > 0:
            self.texture = self.textura_direita
        elif self.change_x < 0:
            self.texture = self.textura_esquerda

        if self.right > 800:
            self.change_x = 0
            self.right = 800

        if self.top > 600:
            self.change_y = 0
            self.top = 600

        if self.left < 0:
            self.change_x = 0
            self.left = 0

        if self.bottom < 0:
            self.change_y = 0
            self.bottom = 0


class Moeda(arcade.Sprite):
    def __init__(self):
        super().__init__("moeda.png", scale=0.2)

    def update(self, delta_time):

        if self.center_x > 800:
            self.change_x *= -1

        if self.center_x < 0:
            self.change_x *= -1

        if self.center_y > 600:
            self.change_y *= -1

        if self.center_y < 0:
            self.change_y *= -1

        self.center_x += self.change_x
        self.center_y += self.change_y


class Inimigo(arcade.Sprite):
    def __init__(self):
        super().__init__("inimigo.png", scale=0.2)

        self.change_x = random.choice([-5, 5])
        self.change_y = random.choice([-5, 5])

    def update(self, delta_time):

        if self.right >= 800 or self.left <= 0:
            self.change_x *= -1

        if self.top >= 600 or self.bottom <= 0:
            self.change_y *= -1

        self.center_x += self.change_x
        self.center_y += self.change_y


class InimigoEspecial(arcade.Sprite):
    def __init__(self):
        super().__init__("goblin.png", scale=0.175)

        self.change_x = random.choice([-4, 4])
        self.change_y = random.choice([-4, 4])

    def update(self, delta_time):

        if self.right >= 800 or self.left <= 0:
            self.change_x *= -1

        if self.top >= 600 or self.bottom <= 0:
            self.change_y *= -1

        self.center_x += self.change_x
        self.center_y += self.change_y


class JanelaJogo(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Titulo padrão")

        arcade.set_background_color(arcade.color.IRIS)

        self.movimento = 10
        self.pontuacao = 0

        # Jogador
        self.personagem = Jogador()
        self.personagem.center_x = 400
        self.personagem.center_y = 300

        self.sprite_jogador = arcade.SpriteList()
        self.sprite_jogador.append(self.personagem)

        # Moeda móvel
        self.moeda = Moeda()
        self.moeda.center_x = 0
        self.moeda.center_y = 0
        self.moeda.change_x += self.movimento
        self.moeda.change_y += self.movimento

        self.sprite_moeda = arcade.SpriteList()
        self.sprite_moeda.append(self.moeda)

        # Outras moedas
        for i in range(10):
            moeda_simples = Moeda()
            moeda_simples.center_x = random.randint(50, 750)
            moeda_simples.center_y = random.randint(50, 550)

            self.sprite_moeda.append(moeda_simples)

        # Inimigo normal
        self.inimigo = Inimigo()
        self.inimigo.center_x = random.randint(100, 700)
        self.inimigo.center_y = random.randint(100, 500)

        self.sprite_inimigo = arcade.SpriteList()
        self.sprite_inimigo.append(self.inimigo)

        # Goblins
        self.sprite_goblins = arcade.SpriteList()

        for i in range(3):
            goblin = InimigoEspecial()
            goblin.center_x = random.randint(50, 750)
            goblin.center_y = random.randint(50, 550)

            self.sprite_goblins.append(goblin)

    def on_draw(self):
        self.clear()

        self.sprite_jogador.draw()
        self.sprite_moeda.draw()
        self.sprite_inimigo.draw()
        self.sprite_goblins.draw()

        arcade.draw_text(
            f"Moedas Coletadas: {self.pontuacao}",
            10,
            570,
            arcade.color.BLACK,
            14
        )

    def on_update(self, delta_time):

        self.sprite_jogador.update(delta_time)
        self.sprite_moeda.update(delta_time)

        self.sprite_inimigo.update(delta_time)
        self.sprite_goblins.update(delta_time)

        # moedas
        moedas_colididas = arcade.check_for_collision_with_list(
            self.personagem,
            self.sprite_moeda
        )

        for moeda in moedas_colididas:
            moeda.remove_from_sprite_lists()
            self.pontuacao += 1

        # inimigo → perde 3 moedas (sem negativo)
        if arcade.check_for_collision(self.personagem, self.inimigo):
            self.pontuacao -= 3

            if self.pontuacao < 0:
                self.pontuacao = 0

        # goblins → perde 1 moeda
        goblins_colididos = arcade.check_for_collision_with_list(
            self.personagem,
            self.sprite_goblins
        )

        for goblin in goblins_colididos:

            goblin.remove_from_sprite_lists()

            novo_goblin = InimigoEspecial()
            novo_goblin.center_x = random.randint(50, 750)
            novo_goblin.center_y = random.randint(50, 550)

            self.sprite_goblins.append(novo_goblin)

            self.pontuacao -= 1

            if self.pontuacao < 0:
                self.pontuacao = 0

    def on_key_press(self, key, modifiers):

        if key == arcade.key.LEFT:
            self.personagem.change_x -= self.movimento

        if key == arcade.key.RIGHT:
            self.personagem.change_x += self.movimento

        if key == arcade.key.UP:
            self.personagem.change_y += self.movimento

        if key == arcade.key.DOWN:
            self.personagem.change_y -= self.movimento

        if key == arcade.key.ESCAPE:
            self.close()

    def on_key_release(self, key, modifiers):

        if key == arcade.key.RIGHT or key == arcade.key.LEFT:
            self.personagem.change_x = 0

        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.personagem.change_y = 0


def main():
    tela = JanelaJogo()
    arcade.run()


if __name__ == "__main__":
    main()