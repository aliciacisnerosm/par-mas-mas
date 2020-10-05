"""
Proyecto compiladores
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from par_mas_mas.lexer import parser

class parmasmas(toga.App):

    def startup(self):
      main_box = toga.Box(style=Pack(direction=COLUMN))

      name_label = toga.Label(
      'Your name: ',
      style=Pack(padding=(0, 5))
      )
      self.name_input = toga.TextInput(style=Pack(flex=1))

      name_box = toga.Box(style=Pack(direction=ROW, padding=5))
      name_box.add(name_label)
      name_box.add(self.name_input)

      button = toga.Button(
      'Say Hello!',
      on_press=self.say_hello,
      style=Pack(padding=5)
      )

      main_box.add(name_box)
      main_box.add(button)

      self.main_window = toga.MainWindow(title=self.formal_name)
      self.main_window.content = main_box
      self.main_window.show()

    def say_hello(self, widget):
      print(parser())
    
def main():
    return parmasmas()
