from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class MainScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)

        title = Label(
            text="MQChatX",
            font_size=32,
            size_hint=(1, 0.2)
        )

        btn = Button(
            text="شروع",
            size_hint=(1, 0.2)
        )

        self.add_widget(title)
        self.add_widget(btn)


class MQChatX(App):
    def build(self):
        return MainScreen()


if __name__ == "__main__":
    MQChatX().run()
