from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class MainScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", spacing=10, padding=10, **kwargs)

        self.title = Label(
            text="MQChatX",
            font_size=30,
            size_hint=(1, 0.1)
        )

        self.chat = Label(
            text="",
            halign="left",
            valign="top",
            size_hint=(1, 0.6)
        )

        self.message = TextInput(
            hint_text="پیام خود را بنویسید...",
            multiline=False,
            size_hint=(1, 0.15)
        )

        self.send = Button(
            text="ارسال",
            size_hint=(1, 0.15)
        )

        self.send.bind(on_press=self.send_message)

        self.add_widget(self.title)
        self.add_widget(self.chat)
        self.add_widget(self.message)
        self.add_widget(self.send)

    def send_message(self, instance):
        text = self.message.text.strip()

        if text:
            self.chat.text += f"\n👤 شما: {text}"
            self.message.text = ""
