# Import required libraries
import kivy
kivy.require(kivy.__version__)
import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.core.window import Window
Window.clearcolor = (1, 1, 1, 1)

class DieSimulator(App):
    def build(self):
        # For some reason I can't make this a normal variable, because it will give an error related to the scope of the variable
        log = [0]
        def callback(instance):
            # Generate a number different from the one previously generated and show the corresponding image
            die_num = log[-1]
            while die_num == log[-1]:
                die_num = random.randint(1, 6)
            log.append(die_num)
            log.pop(0);
            die_filename = f"images/die{str(die_num)}.png"
            print(die_filename)
            die_image.source = die_filename
            prev_die_num = die_num
            
        # Create the box layout and add an Image widget and the roll button
        self.title = 'Die Simulator'
        layout = BoxLayout(orientation='vertical')
        roll_button = Button(text='Roll')
        roll_button.bind(on_press=callback)
        die_image = Image()
        layout.add_widget(die_image)
        layout.add_widget(roll_button)
        return layout
DieSimulator().run()
