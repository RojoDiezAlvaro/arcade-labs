
# Import the "arcade" library
import arcade
import random

rectangulos = []
def pantallazo(x,y):
    #256/2 = 128
    #144/2 = 72
    arcade.draw_rectangle_filled(x,y,256,144,[53,126,199])
    arcade.draw_rectangle_outline(x,y,256,144,arcade.color.GRAY,3)

    arcade.draw_circle_filled(x-128+32, y-72+112, 3, arcade.color.WHITE)
    arcade.draw_circle_filled(x-128+32, y-72+95, 3, arcade.color.WHITE)

    arcade.draw_arc_outline(x-128+48, y-72+103, 13, 35, arcade.color.WHITE, 90, 270, 3)
    arcade.draw_rectangle_filled(x-128+40, y-72+40, 20, 20, arcade.color.WHITE)

    arcade.draw_rectangle_filled(x-128+35, y-72+35, 4, 4, arcade.color.BLACK)
    arcade.draw_rectangle_filled(x-128+35, y-72+45, 4, 4, arcade.color.BLACK)
    arcade.draw_rectangle_filled(x-128+45, y-72+35, 4, 4, arcade.color.BLACK)
    arcade.draw_rectangle_filled(x-128+45, y-72+45, 4, 4, arcade.color.BLACK)

    arcade.draw_rectangle_filled(x-128+42, y-72+43, 3, 3, arcade.color.BLACK)
    arcade.draw_rectangle_filled(x-128+38, y-72+42, 2, 2, arcade.color.BLACK)
    arcade.draw_rectangle_filled(x-128+42, y-72+39, 2, 2, arcade.color.BLACK)
    arcade.draw_rectangle_filled(x-128+39, y-72+38, 3, 3, arcade.color.BLACK)

    arcade.draw_rectangle_filled(x-128+105, y-72+65, 150, 2, arcade.color.WHITE)
    arcade.draw_rectangle_filled(x-128+80, y-72+75, 100, 2, arcade.color.WHITE)
    arcade.draw_rectangle_filled(x-128+45, y-72+55, 30, 2, arcade.color.WHITE)


def on_draw(delta_time):
    for x, y in rectangulos:
        pantallazo(x, y)

        # Add a new rectangle at a random position
    x = random.randint(128, 896)
    y = random.randint(72, 648)
    rectangulos.append((x, y))  # Store the new rectangle
    pantallazo(x, y)  # Draw it


def main():
    arcade.open_window(1024, 720, "Drawing test2")
    arcade.set_background_color(arcade.color.BLACK)

    arcade.schedule(on_draw,1/15)

    arcade.run()

main()
