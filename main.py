# Import required libraries
import kivy
kivy.require(kivy.__version__)
import random
import time
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle, Ellipse
from kivy.core.window import Window
from kivy.clock import Clock
Window.clearcolor = (1, 1, 1, 1)

class DieSimulator(App):
    def draw_face(self, number):
        # die_size is the size of the die, dot_size is the size of each dot and dist is the distance between the dots and between a dot and the edge of the self.die
        die_size = 400
        dot_size = 80
        dist = 40
        x = self.die.x + (self.die.width - die_size) / 2;
        y = self.die.y + (self.die.height - die_size) / 2;
        with self.die.canvas:
            Color(0, 0.6, 1)
            Rectangle(pos=(x, y), size=(die_size, die_size))
            Color(1, 1, 1)
            # Generate a random number from 1 to 6 and generate a matrix where 1 represents a dot and 0 represents no dot
            num = random.randint(1, 6)
            if (num == 1):
                face = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
            elif (num == 2):
                face = [[1, 0, 0], [0, 0, 0], [0, 0, 1]]
            elif (num == 3):
                face = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
            elif (num == 4):
                face = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
            elif (num == 5):
                face = [[1, 0, 1], [0, 1, 0], [1, 0, 1]]
            else:
                face = [[1, 1, 1], [0, 0, 0], [1, 1, 1]]
            # Draw the dots according to the matrix
            for l in range(3):
                for c in range(3):
                    if (face[l][c] == 1):
                        Ellipse(pos=(x + dist * (c + 1) + dot_size * c, y + dist * (l + 1) + dot_size * l), size=(dot_size, dot_size))
        
    def start_roll(self, instance):
        # Roll the die every 0.1 seconds
        self.count = 0
        Clock.schedule_interval(self.roll_step, 0.1)
        
    def roll_step(self, elapsed):
        # Roll the die
        num = random.randint(1, 6)
        self.draw_face(num)
        self.count += 1
        # If the die has been rolled 5 times then stop
        if (self.count >= 5):
            Clock.unschedule(self.roll_step)
    
    def build(self): 
        # Create the box layout and add an Image widget and the roll button
        self.title = 'Die Simulator'
        layout = BoxLayout(orientation='vertical')
        roll_button = Button(text='Roll', size_hint=(1, 0.5))
        roll_button.bind(on_press=self.start_roll)
        self.die = Widget(size_hint=(1, 0.5))
        layout.add_widget(self.die)
        layout.add_widget(roll_button)
        return layout
DieSimulator().run()
