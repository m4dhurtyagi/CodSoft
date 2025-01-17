from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.widget import Widget
from kivy.storage.jsonstore import JsonStore
from kivy.uix.recycleview import RecycleView
from kivy.clock import Clock

class AddNewForm(Widget):
    text_input = ObjectProperty(None)

    input = StringProperty('')

    store = JsonStore("data.json")

    def submit_input(self):
        self.input = self.text_input.text
        print("Assign input: {}".format(self.input))
        self.save()
        self.input = ''

    def save(self):
        self.store.put(self.input)


class Menu(BoxLayout):
    manager = ObjectProperty(None)


class MyRecycleView(RecycleView):

    def __init__(self, **kwargs):
        super(MyRecycleView, self).__init__(**kwargs)
        self.load_data()
        Clock.schedule_interval(self.load_data, 1)

    def load_data(self, *args):
        store = JsonStore("data.json")
        list_data = []
        for item in store:
            list_data.append({'text': item})

        self.data = list_data


class HomeScreen(Screen):
    pass


class AddScreen(Screen):
    def __init__(self, **kwargs):
        super(AddScreen, self).__init__(**kwargs)
        self.addNewForm = AddNewForm()
        self.add_widget(self.addNewForm)


class ScreenManagement(ScreenManager):
    screen_home = ObjectProperty(None)
    screen_add = ObjectProperty(None)


class TodoApp(App):
    pass

if __name__ == '__main__':
    TodoApp().run()