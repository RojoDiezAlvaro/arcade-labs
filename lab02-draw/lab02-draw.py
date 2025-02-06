
# Import the "arcade" library
import arcade

arcade.open_window(256, 144, "Drawing test2")
arcade.set_background_color([53,126,199])

arcade.start_render()

arcade.draw_circle_filled(32, 112, 3, arcade.color.WHITE)
arcade.draw_circle_filled(32, 95, 3, arcade.color.WHITE)

arcade.draw_arc_outline(48, 103, 13, 35, arcade.color.WHITE, 90, 270, 3)
arcade.draw_rectangle_filled(40,40,20,20,arcade.color.WHITE)

arcade.draw_rectangle_filled(35,35,4,4,arcade.color.BLACK)
arcade.draw_rectangle_filled(35,45,4,4,arcade.color.BLACK)
arcade.draw_rectangle_filled(45,35,4,4,arcade.color.BLACK)
arcade.draw_rectangle_filled(45,45,4,4,arcade.color.BLACK)

arcade.draw_rectangle_filled(42,43,3,3,arcade.color.BLACK)
arcade.draw_rectangle_filled(38,42,2,2,arcade.color.BLACK)
arcade.draw_rectangle_filled(42,39,2,2,arcade.color.BLACK)
arcade.draw_rectangle_filled(39,38,3,3,arcade.color.BLACK)


arcade.draw_rectangle_filled(105,65,150,2,arcade.color.WHITE)
arcade.draw_rectangle_filled(80,75,100,2,arcade.color.WHITE)
arcade.draw_rectangle_filled(45,55,30,2,arcade.color.WHITE)

# --- Finish drawing ---
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()

