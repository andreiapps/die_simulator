import kivy
kivy.require(kivy.__version__)
import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.core.window import Window
Window.clearcolor = (1, 1, 1, 1)

class DiceSimulator(App):
    def build(self):
        log = [0]
        def callback(instance):
            dice_num = log[-1]
            while (dice_num == log[-1]):
                dice_num = random.randint(1, 6)
            log.append(dice_num)
            dice_filename = f"images/die{str(dice_num)}.png"
            print(dice_filename)
            dice_image.source = dice_filename
            prev_dice_num = dice_num
            
        self.title = 'Dice Simulator'
        layout = BoxLayout(orientation='vertical')
        roll_button = Button(text='Roll')
        roll_button.bind(on_press=callback)
        layout.add_widget(roll_button)
        dice_image = Image()
        layout.add_widget(dice_image)
        return layout

DiceSimulator().run()
