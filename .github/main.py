from kivy.app import App
from ui import MainScreen


class MQChatX(App):
    def build(self):
        return MainScreen()


if __name__ == "__main__":
    MQChatX().run()
