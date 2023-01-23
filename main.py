from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

class MainApp(MDApp):
    def build(self):
        self.icon = "title.png"
        self.title = "График работы"
        label = MDLabel(text="Добро пожаловать", halign="center")
        return label

if __name__ == '__main__':
    app = MainApp()
    app.run()