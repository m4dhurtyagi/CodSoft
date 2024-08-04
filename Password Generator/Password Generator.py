import secrets
import string
import random
import re
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
Window.size = (700, 300)

class MyGrid(Widget):
    def PasswordGen(self, passlen):
        if passlen:
            try:
                letters = string.ascii_letters
                digits = string.digits
                special_chars = string.punctuation
                selection_list = letters + digits + special_chars

                passlen = int(passlen)
                global password

                if passlen <=0 or passlen > 30:
                    password = "Enter Valid Length"
                else:
                    password = ''
                    for i in range(passlen):
                        password+= ''.join(secrets.choice(selection_list))
            
            except ValueError:
                password = "Enter Valid Input"

            content = BoxLayout(orientation='vertical')
            content.add_widget(Label(text=password))
            save_button = Button(text='Save and Close', size_hint=(1, 0.2))
            save_button.bind(on_press=self.save)
            content.add_widget(save_button)
            close_button = Button(text='Close', size_hint=(1, 0.2))
            close_button.bind(on_press=self.close_popup)
            content.add_widget(close_button)
            
            self.popup = Popup(title='Password', content=content,size_hint=(None, None), size=(300, 300), auto_dismiss=False)     
            self.popup.open()

    def close_popup(self, instance):
        self.popup.dismiss()  

    def save(self, instance):
        f = open("password.txt", "a+")
        f.write(password + "\n")
        f.close()
        self.close_popup(instance)

class PassGenApp(App):
    def build(self):
        return MyGrid()
    
if __name__ == "__main__":
    PassGenApp().run()
