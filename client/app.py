import tkinter as tk
import ttkbootstrap as ttk
from dotenv import dotenv_values
from yaml import load, Loader
from entities.config import Config
from screens.main import MainScreen
from utils.logger import Logger


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("400x600")
        self.resizable(False, False)
        self.title("Voice Recognition")
        self.config_env = dotenv_values('configs/.env')
        with open('configs/config.yaml', encoding='utf-8') as file:
            self.config_yaml = load(file, Loader=Loader)
        self.config = Config(self.config_env, self.config_yaml)
        self.logging = Logger(self.config)
        self.logging.app.debug('Loaded config: %s',
                               self.config.styles.__dict__)
        ttk.Style().theme_use('superhero')

    def render(self):
        root_frame = ttk.Frame(
            self,
            **self.config.styles.root_frame
        )
        root_frame.place(x=0, y=0)
        MainScreen(root_frame, self.config, self.logging).render_screen()

    def run(self):
        self.render()
        self.mainloop()


if __name__ == "__main__":
    app = App()
    app.run()
