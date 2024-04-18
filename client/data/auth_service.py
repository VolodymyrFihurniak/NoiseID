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
#     print(f'Signal {i}')
#     print(f'Skewness: {pd.Series(signal).skew()}')
#     print(f'Kurtosis: {pd.Series(signal).kurtosis()}')


# #  Perform linear autocorrelation
# autocorrelations = []
# for i, signal in enumerate(signals):
#     autocorrelation = acf(signal, nlags=10000)
#     autocorrelations.append(autocorrelation)
#     # plt.plot(autocorrelations[i][0:10000])
#     # plt.title(f'Signal {i} Autocorrelation')
#     # plt.show()

# # Create a bitmap
# bitmaps = []
# for i, autocorrelation in enumerate(autocorrelations):
#     bitmap = np.where(autocorrelation > 0.5, 1, 0)
#     bitmaps.append(bitmap)
#     # plt.plot(bitmaps[i][0:10000])
#     # plt.title(f'Signal {i} Bitmap')
#     # plt.show()

# # Compare the bit patterns and find the Hamming distance

# for i in range(max_signals):
#     for j in range(i + 1, max_signals):
#         hamming_distance = np.sum(bitmaps[i] != bitmaps[j])
#         print(f'Hamming distance between signal {
#               i} and signal {j}: {hamming_distance}')

# # Output device

# # for i in range(pyaudio.PyAudio().get_device_count()):
# #     device = pyaudio.PyAudio().get_device_info_by_index(i)
# #     print(f'Index: {i}, Name: {device['name']}')

import pandas as pd
import numpy as np
import requests as req


from statsmodels.tsa.stattools import acf
from core.microphone_recorder import Microphone, MicrophoneRecorder
from dtos.user_dto import UserDTO
from entities.config import Config
from utils.logger import Logger


class AuthService:
    def __init__(self, logging: Logger, config: Config) -> None:
        self.logging = logging
        self.config = config

    def record_voice(self, microphone: Microphone, rate: int, frames_per_buffer: int, duration: int) -> np.ndarray:
        recorder = MicrophoneRecorder(microphone)
        audio = recorder.record(rate, frames_per_buffer, duration)
        return np.frombuffer(audio, dtype=np.int16)

    def calculate_skewness(self, signal: np.ndarray) -> float:
        return pd.Series(signal).skew()

    def calculate_kurtosis(self, signal: np.ndarray) -> float:
        return pd.Series(signal).kurtosis()

    def calculate_autocorrelation(self, signal: np.ndarray, nlags: int) -> np.ndarray:
        return acf(signal, nlags=nlags)

    def create_bitmap(self, autocorrelation: np.ndarray) -> np.ndarray:
        return np.where(autocorrelation > 0.5, 1, 0)

    def calculate_hamming_distance(self, bitmap1: np.ndarray, bitmap2: np.ndarray) -> int:
        return np.sum(bitmap1 != bitmap2)

    def login(self, user: UserDTO, microphone: Microphone) -> str:
        signals = []
        autocorrelations = []
        bitmaps = []

        accepted_signals = 0
        for i in range(self.config.microphone.max_signals):
            signal = self.record_voice(
                microphone,
                self.config.microphone.rate,
                self.config.microphone.frames_per_buffer,
                self.config.microphone.duration
            )

            skewness = self.calculate_skewness(signal)
            kurtosis = self.calculate_kurtosis(signal)

            if skewness > 0.5 or kurtosis > 0.5:
                self.logging.business.info(f'Anomaly detected in signal {i}')
                continue

            signals.append(signal)
            accepted_signals += 1
            self.logging.business.info(f'Signal {i}')
            self.logging.business.info(f'Skewness: {skewness}')
            self.logging.business.info(f'Kurtosis: {kurtosis}')

            autocorrelation = self.calculate_autocorrelation(signal, 10000)
            autocorrelations.append(autocorrelation)

            bitmap = self.create_bitmap(autocorrelation)
            bitmaps.append(bitmap)

        sorted_signals = sorted(
            signals, key=lambda signal: pd.Series(signal).skew())

        self.logging.business.info('Sorted signals:')
        for i, signal in enumerate(sorted_signals):
            self.logging.business.info(f'Signal {i}')
            self.logging.business.info(f'Skewness: {pd.Series(signal).skew()}')
            self.logging.business.info(
                f'Kurtosis: {pd.Series(signal).kurtosis()}')
            self.logging.business.info('')
        user.data = np.array(sorted_signals[0], dtype=np.int16).tobytes()
        stream_data = {'stream': user.data}
        process = req.post(
            f'http://{self.config.app.server_domain}:'
            f'{self.config.app.server_port}/api/auth/login',
            params=user.to_dict(),
            files=stream_data,
            timeout=60
        )
        return 'Success' if process.status_code == 200 else 'Failed'
