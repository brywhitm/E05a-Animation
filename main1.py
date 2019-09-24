#Copy the contents from http://arcade.academy/examples/move_mouse.html#move-mouse and see if you can figure out what is going on. Add comments to any uncommented lines
"""
This simple animation example shows how to move an item with the mouse, and
handle mouse clicks.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.move_mouse
"""

import arcade   #imports the arcade modual

SCREEN_WIDTH = 640      #sets screen size
SCREEN_HEIGHT = 480     #^
SCREEN_TITLE = "Move Mouse Example"     #sets title of the screen created


class Ball:     #creates a class for ball
    def __init__(self, position_x, position_y, radius, color):      #a function created that has many parameters

        # Take the parameters of the init function above, and create instance variables out of them.
        self.position_x = position_x        #self refers to the class item ball. position for the x axis is set to position_x
        self.position_y = position_y        #sets the class item ball's position on the y axis
        self.radius = radius        #sets the ball's radius to radius
        self.color = color      #sets the ball's color to color
                                                        #position,radius and color are defined later and are called back here
    def draw(self):     #a function creating the circle
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)


class MyGame(arcade.Window):    #creates a class for the game window

    def __init__(self, width, height, title):   #a function created that has many parameters

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.ASH_GREY)      #sets windows background to a color

        # Create our ball
        self.ball = Ball(50, 50, 15, arcade.color.AUBURN)

    def on_draw(self):  #when the window open
        """ Called whenever we need to draw the window. """
        arcade.start_render()
        self.ball.draw()

    def on_mouse_motion(self, x, y, dx, dy):
        """ Called to update our objects. Happens approximately 60 times per second."""
        self.ball.position_x = x        #sets position for the ball
        self.ball.position_y = y        #^

    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called when the user presses a mouse button.
        """
        print(f"You clicked button number: {button}")       #prints the string and the number of button pressed
        if button == arcade.MOUSE_BUTTON_LEFT:          #make it so if the left mouse button is pressed then
            self.ball.color = arcade.color.BLACK        #change the balls color to black

    def on_mouse_release(self, x, y, button, modifiers):
        """
        Called when a user releases a mouse button.
        """
        if button == arcade.MOUSE_BUTTON_LEFT:      #when the left mouse button is released then
            self.ball.color = arcade.color.AUBURN        #change the balls color to auburn


def main():     #main function used for loop
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)      #sets up the window
    arcade.run()        #tells it to run arcade


if __name__ == "__main__":      #make the program go back to main() basicly making a loop
    main()