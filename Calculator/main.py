import re
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
Window.size = (300, 500)

class CustomTextInput(TextInput):
    pat = re.compile('[^0-9\+\-\*/\(\)\.]')
    def insert_text(self, substring, from_undo=False):
        pat = self.pat
        if '.' in self.text:
            s = re.sub(pat, '', substring)
        else:
            s = '.'.join(
                re.sub(pat, '', s)
                for s in substring.split('.', 1)
            )
        return super().insert_text(s, from_undo=from_undo)
    
    def on_text_validate(self):
        self.parent.parent.calculate(self.text)

    def on_parent(self, widget, parent):
        self.focus = True

class MyGrid(Widget):
    def calculate(self, calculation):
        if calculation:
            try:
                self.display.text = str(eval(calculation))
            except Exception:
                self.display.text = "Invalid Expression"

class CalculatorApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    CalculatorApp().run()
