import tkinter as tk
import ttkbootstrap as ttk
from entities.config import Config
from controllers.auth_controller import AuthController
from core.microphone_recorder import Microphone


class MainScreen():
    def __init__(self, master_frame: tk.Frame, config: Config, logging):
        self.master_frame = master_frame
        self.config = config
        self.logging = logging

    def create_frame(self, master_frame):
        return tk.Frame(
            master_frame,
            **self.config.styles.main_frame
        )

    def screen(self):
        frame = self.create_frame(self.master_frame)
        frame.place(x=10, y=50)

        mic = Microphone().get_microphone()
        choose_microphone_label = ttk.Label(frame, text="Choose microphone:")
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

        username_label = ttk.Label(frame, text="Username:")
        username_entry = ttk.Entry(frame, width=37)
        password_label = ttk.Label(frame, text="Password:")
        password_entry = ttk.Entry(frame, width=37, show='*')
        process_information_area = ttk.Label(
            frame, text="Status authentication: ")

        def send_process():
            contoller = AuthController(self.logging, self.config).login(
                username_entry.get(),
                password_entry.get(),
                Microphone(mics_list.current(), mics_list.get())
            )
            process_information_area.config(
                text=f"Status authentication: {contoller['message']}")

        process_button = ttk.Button(
            frame,
            text="Record",
            command=send_process
        )

        choose_microphone_label.grid(row=0, column=0)
        mics_list.grid(row=0, column=1)
        username_label.grid(row=1, column=0)
        username_entry.grid(row=1, column=1)
        password_label.grid(row=2, column=0)
        password_entry.grid(row=2, column=1)
        process_information_area.grid(row=4, column=0, columnspan=2)
        process_button.grid(row=3, column=0, columnspan=2)

    def render_screen(self):
        self.screen()
