import pyaudio
import numpy as np


class TonesPlayer:
    __tone_freq = {"c1": 261.63,
                   "d1": 293.66, "e1": 329.63, "f1": 349.23, "g1": 392.00, "a1": 440.00, "h1": 493.88, "c2": 523.25,
                   "d2": 587.33, "e2": 659.26, "f2": 698.46, "g2": 783.99, "a2": 880.00, "h2": 987.77, "c3": 1046.50}

    def __init__(self, volume, sample_rate, duration):
        self.__volume = volume
        self.__sample_rate = sample_rate
        self.__duration = duration

    def play(self):
        p = pyaudio.PyAudio()

        samples = (np.sin(2 * np.pi * np.arange(self.__sample_rate * self.__duration) * self.__tone_freq["c1"] / self.__sample_rate)).astype(np.float32)
        samples1 = (np.sin(2 * np.pi * np.arange(self.__sample_rate * self.__duration) * self.__tone_freq["d1"] / self.__sample_rate)).astype(np.float32)
        samples2 = (np.sin(2 * np.pi * np.arange(self.__sample_rate * self.__duration) * self.__tone_freq["e1"] / self.__sample_rate)).astype(np.float32)
        samples3 = (np.sin(2 * np.pi * np.arange(self.__sample_rate * self.__duration) * self.__tone_freq["f1"] / self.__sample_rate)).astype(np.float32)

        stream = p.open(format=pyaudio.paFloat32,
                        channels=1,
                        rate=self.__sample_rate,
                        output=True)

        stream.write(self.__volume * samples)
        stream.write(self.__volume * samples1)
        stream.write(self.__volume * samples2)
        stream.write(self.__volume * samples3)

        stream.stop_stream()
        stream.close()

        p.terminate()
