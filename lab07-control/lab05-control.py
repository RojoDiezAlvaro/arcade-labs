""" Lab 7 - User Control """

import arcade
import random


# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 3
DEAD_ZONE = 0.02



def draw_dirt_floor():
    """Draw the dirt floor with random stones."""
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT, 0, arcade.color.BROWN_NOSE)

    # Draw random stones
    for _ in range(50):  # Adjust the number of stones
        x = random.randint(0, SCREEN_WIDTH)
        y = random.randint(0, SCREEN_HEIGHT)
        size = random.randint(5, 20)
        color = random.choice([arcade.color.GRAY, arcade.color.DARK_GRAY, arcade.color.LIGHT_GRAY])
        arcade.draw_ellipse_filled(x, y, size, size * 0.7, color)

class Ball:
    def __init__(self, position_x, position_y,change_x,change_y, radius, color):

        # Take the parameters of the init function above,
        # and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color
        self.hit = False
        self.chop_sound = arcade.load_sound("WoodChop.wav")
        self.wrong_sound = arcade.load_sound("Wrong.wav")


    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x,
                                  self.position_y,
                                  self.radius,
                                  self.color)

    def on_update(self):
        # Move the ball
        self.position_y += self.change_y
        self.position_x += self.change_x

        # See if the ball hit the edge of the screen. If so, change direction
        if self.position_x < self.radius:
            self.position_x = self.radius
            self.hit = True
        elif self.position_x > SCREEN_WIDTH - self.radius:
            self.position_x = SCREEN_WIDTH - self.radius
            self.hit = True
        elif self.position_y < self.radius:
            self.position_y = self.radius
            self.hit = True
        elif self.position_y > SCREEN_HEIGHT - self.radius:
            self.position_y = SCREEN_HEIGHT - self.radius
            self.hit = True
        else:
            self.hit = False

class MyGame(arcade.Window):
    """ Our Custom Window Class"""
    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")
        self.last_hit = 5
        self.set_mouse_visible(False)
        arcade.set_background_color(arcade.color.BROWN_NOSE)

        joysticks = arcade.get_joysticks()

        # If we have a game controller plugged in, grab it and
        # make an instance variable out of it.
        if joysticks:
            self.joystick = joysticks[0]
            self.joystick.open()
        else:
            self.joystick = None

        self.stones = [
            (random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT),
             random.randint(3, 15), random.choice([arcade.color.GRAY, arcade.color.DARK_GRAY, arcade.color.LIGHT_GRAY]))
            for _ in range(35)
        ]

        self.trees = [
            (random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT),
             random.randint(30, 80), random.choice([arcade.color.GREEN, arcade.color.GREEN_YELLOW, arcade.color.APPLE_GREEN]))
            for _ in range(15)
        ]

        # Create our ball
        self.ball = Ball(50, 50, 0, 0, 15, arcade.color.BLACK_OLIVE)


    def on_draw(self):
        self.clear()
        # Draw the dirt floor
        arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT, 0, arcade.color.BROWN_NOSE)
        # Draw stones using the stored positions
        for x, y, size, color in self.stones:
            arcade.draw_ellipse_filled(x, y, size, size * 0.7, color)
        self.ball.draw()
        for x, y, size, color in self.trees:
            arcade.draw_ellipse_filled(x, y, size, size * 0.7, color)
        #Esto es a posta, quiero pasar por encima de las piedras y por debajo de los arboles

    def on_update(self, delta_time,):
        self.last_hit += delta_time
        if self.joystick:

            # Set a "dead zone" to prevent drive from a centered joystick
            if abs(self.joystick.x) < DEAD_ZONE:
                self.ball.change_x = 0
            else:
                self.ball.change_x = self.joystick.x * MOVEMENT_SPEED

            # Set a "dead zone" to prevent drive from a centered joystick
            if abs(self.joystick.y) < DEAD_ZONE:
                self.ball.change_y = 0
            else:
                self.ball.change_y = -self.joystick.y * MOVEMENT_SPEED

        if self.ball.hit and self.last_hit > 2:
            self.last_hit = 0
            arcade.sound.play_sound(self.ball.wrong_sound)

        self.ball.on_update()



    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.A:
            self.ball.change_x -= MOVEMENT_SPEED
        elif key == arcade.key.D:
            self.ball.change_x += MOVEMENT_SPEED
        elif key == arcade.key.W:
            self.ball.change_y += MOVEMENT_SPEED
        elif key == arcade.key.S:
            self.ball.change_y -= MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.A:
            self.ball.change_x += MOVEMENT_SPEED
        elif key == arcade.key.D:
            self.ball.change_x -= MOVEMENT_SPEED
        elif key == arcade.key.W:
            self.ball.change_y -= MOVEMENT_SPEED
        elif key == arcade.key.S:
            self.ball.change_y += MOVEMENT_SPEED

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        arcade.sound.play_sound(self.ball.chop_sound)

def main():
    window = MyGame()
    arcade.run()


main()


