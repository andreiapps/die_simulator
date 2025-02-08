# Import needed libraries
import kivy
kivy.require(kivy.__version__)
import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.core.window import Window
Window.clearcolor = (1, 1, 1, 1)

# App class
class DieSimulator(App):
    def build(self):
        log = [0]
        # The callback function will run when the button is clicked
        def callback(instance):
            # Generate a number, making sure it's different from the previous one
            while dice_num == prev_dice_num:
                dice_num = random.randint(1, 6)
            # Load the image
            dice_filename = f"images/die{str(dice_num)}.png"
            dice_image.source = dice_filename
            prev_dice_num = dice_num

        # Create a BoxLayout and add the widgets(an Image object to display the die and the roll button)
        self.title = 'Dice Simulator'
        layout = BoxLayout(orientation='vertical')
        roll_button = Button(text='Roll')
        roll_button.bind(on_press=callback)
        layout.add_widget(roll_button)
        dice_image = Image()
        layout.add_widget(dice_image)
        return layout

DieSimulator().run()
