from kivymd.app import App
from kivy.lang import Builder
from kivymd.uix.boxlayout import BoxLayout

KV = '''
MyBox:
    Button:
        text: 'Button_1'
        
'''

class MyBox(BoxLayout):
    pass


class MainApp(App):
    def build(self):
        return Builder.load_string(KV)

if __name__ == '__main__':
    MainApp().run()