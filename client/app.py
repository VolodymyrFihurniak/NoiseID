# import pyaudio
# import time
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# # from matplotlib.animation import FuncAnimation
# from statsmodels.tsa.stattools import acf
# from core.microphone_recorder import Microphone, MicrophoneRecorder

# device = Microphone(2, 'Microphone (Line In Audio Device)')
# recorder = MicrophoneRecorder(device)

# # Record and plot voice

# rate = 44100
# frames_per_buffer = 2048
# duration = 1

# # audio = recorder.record(rate, frames_per_buffer, duration)
# # audio = np.frombuffer(audio, dtype=np.int16)

# max_signals = 5
# signals = []


# for i in range(max_signals):
#     audio = recorder.record(rate, frames_per_buffer, duration)
#     # strip first 44100 samples
#     audio = audio[44100:]
#     audio = np.frombuffer(audio, dtype=np.int16)
#     signals.append(audio)

# signals = np.array(signals)

# # The difference between the distribution of electrical noise voltage amplitudes and the Gaussian distribution is characterized by the values of asymmetry (skew(x)) and kurtosis (kurt(x)), which are calculated according to the formulas:

# for i, signal in enumerate(signals):
#     print(f"Signal {i}")
#     print(f"Skewness: {pd.Series(signal).skew()}")
#     print(f"Kurtosis: {pd.Series(signal).kurtosis()}")


# #  Perform linear autocorrelation
# autocorrelations = []
# for i, signal in enumerate(signals):
#     autocorrelation = acf(signal, nlags=10000)
#     autocorrelations.append(autocorrelation)
#     # plt.plot(autocorrelations[i][0:10000])
#     # plt.title(f"Signal {i} Autocorrelation")
#     # plt.show()

# # Create a bitmap
# bitmaps = []
# for i, autocorrelation in enumerate(autocorrelations):
#     bitmap = np.where(autocorrelation > 0.5, 1, 0)
#     bitmaps.append(bitmap)
#     # plt.plot(bitmaps[i][0:10000])
#     # plt.title(f"Signal {i} Bitmap")
#     # plt.show()

# # Compare the bit patterns and find the Hamming distance

# for i in range(max_signals):
#     for j in range(i + 1, max_signals):
#         hamming_distance = np.sum(bitmaps[i] != bitmaps[j])
#         print(f"Hamming distance between signal {
#               i} and signal {j}: {hamming_distance}")

# # Output device

# # for i in range(pyaudio.PyAudio().get_device_count()):
# #     device = pyaudio.PyAudio().get_device_info_by_index(i)
# #     print(f"Index: {i}, Name: {device['name']}")


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
        MainScreen(root_frame, self.config).render_screen()

    def run(self):
        self.render()
        self.mainloop()


if __name__ == "__main__":
    app = App()
    app.run()
