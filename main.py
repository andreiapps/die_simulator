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
        log = [0]
        def callback(instance):
            die_num = log[-1]
            while (die_num == log[-1]):
                die_num = random.randint(1, 6)
            log = [dice_num]
            dice_filename = f"images/die{str(die_num)}.png"
            print(die_filename)
            die_image.source = die_filename
            prev_die_num = die_num
            
        self.title = 'Die Simulator'
        layout = BoxLayout(orientation='vertical')
        roll_button = Button(text='Roll')
        roll_button.bind(on_press=callback)
        layout.add_widget(roll_button)
        die_image = Image()
        layout.add_widget(dice_image)
        return layout
DiceSimulator().run()
