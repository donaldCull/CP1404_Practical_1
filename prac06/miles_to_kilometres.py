"""
Kivy GUI program to convert miles to Kilometres
Donald Cull
Started 5/09/2016
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

__author__ = 'Donald Cull'


class MilesToKilometresApp(App):
    """MilesToKilometresApp is a Kivy App to convert Miles to Kilometres """

    def build(self):
        Window.size = (200, 100)
        self.title = "Miles to Kilometres"
        self.root = Builder.load_file('miles_to_kilometres.kv')
        return self.root
    def handle_calculate(self, value):
        result = value * 1.60934
        self.root.ids.output_number.text = str("{:.3f}".format(result))
    def handle_increment(self, value):
        positive_increment = value + 1
        self.root.ids.input_number.text = int(positive_increment)



MilesToKilometresApp().run()
