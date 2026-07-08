from kivy.app import App
from kivy.uix.label import Label


class MQChatX(App):
    def build(self):
        return Label(text="سلام! به MQChatX خوش آمدید.")


if __name__ == "__main__":
    MQChatX().run()
