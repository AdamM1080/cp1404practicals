"""
CP1404/CP5632, Practical
Dynamically create buttons based on content of list
Adam Maclean
Estimated time: 30 minutes
Actual time: 30 minutes
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """Main program - Kivy app to create dynamic widgets with labels from list"""

    def __init__(self, **kwargs):
        """Constructor for main app"""
        super(DynamicLabelsApp, self).__init__(**kwargs)
        self.names = ['Adam Maclean', 'Dennis Ritchie', 'Isaac Asimov', 'Albert Camus', 'Duke Nukem', 'John Romero',
                      'Alejandro Jodorowsky', 'Fyodor Dostoyevsky']

    def build(self):
        self.title = 'Dynamic Labels'
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create dynamic labels from list"""
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)


DynamicLabelsApp().run()
