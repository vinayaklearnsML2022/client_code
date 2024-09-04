from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
from twitter_pw import playwright
import socket
import threading

class ClientApp(App):
    def build(self):
        self.message_queue = []
        self.socket_thread = threading.Thread(target=self.receive_messages)
        self.socket_thread.daemon = True
        self.socket_thread.start()

        layout = BoxLayout(orientation='vertical')
        self.text_area = TextInput(size_hint_y=0.9, readonly=True, text="Waiting for messages...\n")
        layout.add_widget(self.text_area)
        
        return layout

    def receive_messages(self):
        host = '127.0.0.1'
        port = 12345
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))
        while True:
            try:
                message = client_socket.recv(1024).decode()
                if message:
                    self.message_queue.append(message)
                    Clock.schedule_once(self.update_text_area)
                    playwright(message)
                else:
                    break
            except:
                break

    def update_text_area(self, dt):
        if self.message_queue:
            self.text_area.text += f"{self.message_queue.pop(0)}\n"

if __name__ == "__main__":
    ClientApp().run()
