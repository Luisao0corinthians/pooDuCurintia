import arcade

class Jogador(arcade.Sprite):
    def __init__(self):
        super().__init__("direita.png", scale= 0.6)

        self.textura_direita = arcade.load_texture("direita.png")
        self.textura_esquerda = arcade.load_texture("esquerda.png")

    def update(self, delta_time):
        self.center_x += self.change_x
        self.center_y += self.change_y


        if self.change_x > 0: 
            self.texture = self.textura_direita
        elif self.change_x < 0:
            self.texture = self.textura_esquerda

class Moeda(arcade.Sprite):
    def __init__(self):
        super().__init__("moeda.png", scale= 0.5)

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

        self.movimento = 1

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

        

    def on_draw(self):
        self.clear()
        self.sprite_jogador.draw()
        self.sprite_moeda.draw()

    def on_update(self, delta_time):
        self.sprite_jogador.update(delta_time)
        self.sprite_moeda.update(delta_time)

def main():
    tela = JanelaJogo()
    arcade.run()

if __name__ == "__main__":
    main()