""" Sprite Sample Program """

import random
import arcade

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = 0.2
COIN_COUNT = 50
MOVEMENT_SPEED = 3
DEAD_ZONE = 0.02


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

        # Variables that will hold sprite lists
        self.player_list = None
        self.coin_list = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0
        self.change_y = 0
        self.change_x = 0

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up the player
        # Character image from kenney.nl
        self.player_sprite = arcade.Sprite("character.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_sprite.margin_x = 20
        self.player_sprite.margin_y = 30
        self.player_list.append(self.player_sprite)

        # Create the coins
        for i in range(COIN_COUNT):

            # Create the coin instance
            # Coin image from kenney.nl
            coin = arcade.Sprite("coin_01.png", SPRITE_SCALING_COIN)

            # Position the coin
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the coin to the lists
            self.coin_list.append(coin)

    def on_draw(self):
        """ Draw everything """
        self.clear()
        self.coin_list.draw()
        self.player_list.draw()
        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_update(self, delta_time):

        self.player_sprite.center_y += self.change_y
        self.player_sprite.center_x += self.change_x

        if self.player_sprite.center_x < self.player_sprite.margin_x:
            self.player_sprite.center_x = self.player_sprite.margin_x
        elif self.player_sprite.center_x > SCREEN_WIDTH - self.player_sprite.margin_x:
            self.player_sprite.center_x = SCREEN_WIDTH - self.player_sprite.margin_x
        elif self.player_sprite.center_y < self.player_sprite.margin_y:
            self.player_sprite.center_y = self.player_sprite.margin_y
        elif self.player_sprite.center_y > SCREEN_HEIGHT - self.player_sprite.margin_y:
            self.player_sprite.center_y = SCREEN_HEIGHT - self.player_sprite.margin_y

        self.coin_list.update()
        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite,self.coin_list)
        for coin in coins_hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.A:
            self.change_x -= MOVEMENT_SPEED
        elif key == arcade.key.D:
            self.change_x += MOVEMENT_SPEED
        elif key == arcade.key.W:
            self.change_y += MOVEMENT_SPEED
        elif key == arcade.key.S:
            self.change_y -= MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.A:
            self.change_x += MOVEMENT_SPEED
        elif key == arcade.key.D:
            self.change_x -= MOVEMENT_SPEED
        elif key == arcade.key.W:
            self.change_y -= MOVEMENT_SPEED
        elif key == arcade.key.S:
            self.change_y += MOVEMENT_SPEED

def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()