import pyaudio


class Microphone:
    def __init__(self, index: int = 0, name: str = 'Setup Microphone') -> None:
        self._index = index
        self.name = name

    def __str__(self) -> str:
        return f"Index: {self._index}, Name: {self.name}"

    @property
    def index(self) -> int:
        return self._index

    @index.setter
    def index(self, index: int) -> None:
        self._index = index

    @staticmethod
    def return_devices() -> dict:
        devices = {}
        for i in range(pyaudio.PyAudio().get_device_count()):
            device = pyaudio.PyAudio().get_device_info_by_index(i)
            devices[i] = device['name']
        return devices

    @staticmethod
    def get_microphone(index: int = 0):
        devices = Microphone.return_devices()
        return Microphone(index, devices[index])


class MicrophoneRecorder:
    def __init__(self, microphone: Microphone):
        self.microphone = microphone

    def record(self, rate: int, frames_per_buffer: int, duration: int) -> bytes:
        audio = pyaudio.PyAudio()
        stream = audio.open(
            format=pyaudio.paInt16,
            channels=1,
            rate=rate,
            input=True,
            input_device_index=self.microphone.index,
            frames_per_buffer=frames_per_buffer
        )

        frames = []
        for _ in range(0, int(rate / frames_per_buffer * duration)):
            data = stream.read(frames_per_buffer)
            frames.append(data)

        stream.stop_stream()
        stream.close()
        audio.terminate()

        return b''.join(frames)
