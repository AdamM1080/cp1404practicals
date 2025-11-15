"""
CP1404/CP5632 Practical
Kivy GUI program to convert miles to kilometres
Adam Maclean, IT@JCU
Estimated time: 30 minutes
Actual time: 30 minutes
"""

from kivy.app import App
from kivy.lang import Builder

MILES_TO_KILOMETRES = 1.60934

class ConvertMilesToKilometresApp(App):
    """ ConvertMilesToKilometresApp converts miles to kilometres """
    def build(self):
        """ Build the Kivy app from the kv file """
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculation(self, value):
        """ Handle calculation of miles to kilometres, output result to label widget """
        miles = self.get_valid_miles()
        result = miles * MILES_TO_KILOMETRES
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, increment):
        """Handle incrementation via up/ down buttons"""
        value = self.get_valid_miles() + increment
        self.root.ids.input_miles.text = str(value)
        self.handle_calculation(value)

    def get_valid_miles(self):
        """Get valid input of miles before conversion to kilometres"""
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0.0



ConvertMilesToKilometresApp().run()