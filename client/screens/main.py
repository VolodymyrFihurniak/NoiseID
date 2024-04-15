import tkinter as tk
import ttkbootstrap as ttk
from entities.config import Config
from core.microphone_recorder import MicrophoneRecorder, Microphone


class MainScreen():
    def __init__(self, master_frame: tk.Frame, config: Config):
        self.master_frame = master_frame
        self.config = config

    def create_frame(self, master_frame):
        return tk.Frame(
            master_frame,
            **self.config.styles.main_frame
        )

    def screen(self):
        frame = self.create_frame(self.master_frame)
        frame.place(x=0, y=50)

        mic = Microphone().get_microphone()
        ttk.Label(frame, text="Microphone:").grid(row=0, column=0)
        ttk.Label(frame, text=mic.name).grid(row=0, column=1)
        ttk.Label(frame, text="Choose microphone:").grid(row=1, column=0)
        mics = Microphone.return_devices()
        mics_list = ttk.Combobox(
            frame,
            state='readonly',
            width=35,
            height=10,
            values=list(mics.values()),
            cursor='hand2',
        )
        mics_list.current(mics_list['values'].index(mic.name))
        mics_list.grid(row=1, column=1)

        ttk.Button(
            frame,
            text="Record",
            command=lambda: print(mics_list.current())
        ).grid(row=2, column=0, columnspan=2)

    def render_screen(self):
        self.screen()
