"""
Kivy GUI program to convert miles to Kilometres
Donald Cull
Started 5/09/2016
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

__author__ = 'Donald Cull'

MILES_TO_KILOMETRES = 1.60934


class MilesToKilometresApp(App):
    """MilesToKilometresApp is a Kivy App to convert Miles to Kilometres """

    def build(self):
        Window.size = (200, 100)
        self.title = "Miles to Kilometres"
        self.root = Builder.load_file('miles_to_kilometres.kv')
        return self.root

    def handle_calculate(self):
        value = self.get_valid_miles()
        result = value * MILES_TO_KILOMETRES
        self.root.ids.output_number.text = str(result)

    def handle_increment(self, increment):
        value = self.get_valid_miles() + increment
        self.root.ids.input_number.text = str(value)
        self.handle_calculate()

    def get_valid_miles(self):
        try:
            value = float(self.root.ids.input_number.text)
            return value
        except ValueError:
            return 0


MilesToKilometresApp().run()
