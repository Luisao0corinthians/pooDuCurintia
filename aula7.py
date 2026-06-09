import arcade
import random

class Jogador(arcade.Sprite):
    def __init__(self):
        super().__init__("direita.png", scale= 0.4)

        self.textura_direita = arcade.load_texture("direita.png")
        self.textura_esquerda = arcade.load_texture("esquerda.png")
        self.textura_choro = arcade.load_texture("textura_choro.png")

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
        super().__init__("moeda.png", scale= 0.2)

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
        

class JanelaJogo(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Titulo padrão")
        arcade.set_background_color(arcade.color.AMAZON)

        self.movimento = 10

        self.personagem = Jogador()
        self.personagem.center_x = 400
        self.personagem.center_y = 300
        self.sprite_jogador = arcade.SpriteList()
        self.sprite_jogador.append(self.personagem)

        self.moeda = Moeda()
        self.moeda.center_x = 00
        self.moeda.center_y = 00
        self.moeda.change_x += self.movimento
        self.moeda.change_y += self.movimento

        self.sprite_moeda = arcade.SpriteList()
        self.sprite_moeda.append(self.moeda)

        for i in range(25):
            self.moeda_simples = Moeda()
            self.moeda_simples.center_x = random.randint(50,800-50)
            self.moeda_simples.center_y = random.randint(50,600-50)
            self.sprite_moeda.append(self.moeda_simples)

    def on_draw(self):
        self.clear()
        self.sprite_jogador.draw()
        self.sprite_moeda.draw()

    def on_update(self, delta_time):
        self.sprite_jogador.update(delta_time)
        self.sprite_moeda.update(delta_time)

        if arcade.check_for_collision(self.personagem, self.moeda):
            self.personagem.texture = self.personagem.textura_choro
    
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