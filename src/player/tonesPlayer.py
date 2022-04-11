import numpy as np
from synthesizer import Player, Writer, Synthesizer, Waveform


class TonesPlayer:
    __tone_freq = {"h": 246.94,"c1": 261.63,
                   "d1": 293.66, "e1": 329.63, "f1": 349.23, "g1": 392.00, "a1": 440.00, "h1": 493.88, "c2": 523.25,
                   "d2": 587.33, "e2": 659.26, "f2": 698.46, "g2": 783.99, "a2": 880.00, "h2": 987.77, "c3": 1046.50}
    __waves = []

    def __init__(self, variations, volume):
        self.__variations = variations
        self.synthesizer = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=volume, use_osc2=False)

    def __generate_waves(self, variation):
        for tone in variation:
            if tone == 0:
                self.__waves.append(self.synthesizer.generate_constant_wave(self.__tone_freq["c1"], 4))
            elif tone == 1:
                self.__waves.append(self.synthesizer.generate_constant_wave(self.__tone_freq["c1"], 2))
            elif tone == 2:
                self.__waves.append(self.synthesizer.generate_constant_wave(self.__tone_freq["c1"], 1))
            elif tone == 3:
                self.__waves.append(self.synthesizer.generate_constant_wave(self.__tone_freq["d1"], 4))
            elif tone == 4:
                self.__waves.append(self.synthesizer.generate_constant_wave(self.__tone_freq["d1"], 2))
            elif tone == 5:
                self.__waves.append(self.synthesizer.generate_constant_wave(self.__tone_freq["d1"], 1))
            elif tone == 6:
                self.__waves.append(self.synthesizer.generate_constant_wave(self.__tone_freq["e1"], 4))
            elif tone == 7:
                self.__waves.append(self.synthesizer.generate_constant_wave(self.__tone_freq["e1"], 2))
            elif tone == 8:
                self.__waves.append(self.synthesizer.generate_constant_wave(self.__tone_freq["e1"], 1))
            elif tone == 9:
                self.__waves.append(self.synthesizer.generate_constant_wave(self.__tone_freq["f1"], 4))
            elif tone == 10:
                self.__waves.append(self.synthesizer.generate_constant_wave(self.__tone_freq["f1"], 2))
            elif tone == 11:
                self.__waves.append(self.synthesizer.generate_constant_wave(self.__tone_freq["f1"], 1))
            elif tone == 12:
                self.__waves.append(self.synthesizer.generate_constant_wave(self.__tone_freq["g1"], 4))
            elif tone == 13:
                self.__waves.append(self.synthesizer.generate_constant_wave(self.__tone_freq["g1"], 2))
            elif tone == 14:
                self.__waves.append(self.synthesizer.generate_constant_wave(self.__tone_freq["g1"], 1))
            elif tone == 15:
                self.__waves.append(self.synthesizer.generate_constant_wave(self.__tone_freq["a1"], 4))
            elif tone == 16:
                self.__waves.append(self.synthesizer.generate_constant_wave(self.__tone_freq["a1"], 2))
            elif tone == 17:
                self.__waves.append(self.synthesizer.generate_constant_wave(self.__tone_freq["a1"], 1))
            elif tone == 18:
                self.__waves.append(self.synthesizer.generate_constant_wave(self.__tone_freq["h1"], 4))
            elif tone == 19:
                self.__waves.append(self.synthesizer.generate_constant_wave(self.__tone_freq["h1"], 2))
            elif tone == 20:
                self.__waves.append(self.synthesizer.generate_constant_wave(self.__tone_freq["h1"], 1))
            elif tone == 21:
                self.__waves.append(self.synthesizer.generate_constant_wave(self.__tone_freq["c2"], 4))
            elif tone == 22:
                self.__waves.append(self.synthesizer.generate_constant_wave(self.__tone_freq["c2"], 2))
            elif tone == 23:
                self.__waves.append(self.synthesizer.generate_constant_wave(self.__tone_freq["c2"], 1))
            elif tone == 24:
                pass
            elif tone == 28:
                self.__waves.append(self.synthesizer.generate_constant_wave(self.__tone_freq["d2"], 4))
            elif tone == 29:
                self.__waves.append(self.synthesizer.generate_constant_wave(self.__tone_freq["d2"], 2))
            elif tone == 30:
                self.__waves.append(self.synthesizer.generate_constant_wave(self.__tone_freq["d2"], 1))
            elif tone == 31:
                self.__waves.append(self.synthesizer.generate_constant_wave(self.__tone_freq["e2"], 4))
            elif tone == 32:
                self.__waves.append(self.synthesizer.generate_constant_wave(self.__tone_freq["e2"], 2))
            elif tone == 33:
                self.__waves.append(self.synthesizer.generate_constant_wave(self.__tone_freq["e2"], 1))
            elif tone == 34:
                self.__waves.append(self.synthesizer.generate_constant_wave(self.__tone_freq["f2"], 4))
            elif tone == 35:
                self.__waves.append(self.synthesizer.generate_constant_wave(self.__tone_freq["f2"], 2))
            elif tone == 36:
                self.__waves.append(self.synthesizer.generate_constant_wave(self.__tone_freq["f2"], 1))
            elif tone == 37:
                self.__waves.append(self.synthesizer.generate_constant_wave(self.__tone_freq["g2"], 4))
            elif tone == 38:
                self.__waves.append(self.synthesizer.generate_constant_wave(self.__tone_freq["g2"], 2))
            elif tone == 39:
                self.__waves.append(self.synthesizer.generate_constant_wave(self.__tone_freq["g2"], 1))
            elif tone == 40:
                self.__waves.append(self.synthesizer.generate_constant_wave(self.__tone_freq["a2"], 4))
            elif tone == 41:
                self.__waves.append(self.synthesizer.generate_constant_wave(self.__tone_freq["a2"], 2))
            elif tone == 42:
                self.__waves.append(self.synthesizer.generate_constant_wave(self.__tone_freq["a2"], 1))
            elif tone == 43:
                self.__waves.append(self.synthesizer.generate_constant_wave(self.__tone_freq["h2"], 4))
            elif tone == 44:
                self.__waves.append(self.synthesizer.generate_constant_wave(self.__tone_freq["h2"], 2))
            elif tone == 45:
                self.__waves.append(self.synthesizer.generate_constant_wave(self.__tone_freq["h2"], 1))
            elif tone == 46:
                self.__waves.append(self.synthesizer.generate_constant_wave(self.__tone_freq["c3"], 4))
            elif tone == 47:
                self.__waves.append(self.synthesizer.generate_constant_wave(self.__tone_freq["c3"], 2))
            elif tone == 48:
                self.__waves.append(self.synthesizer.generate_constant_wave(self.__tone_freq["c3"], 1))
            elif tone == 49:
                self.__waves.append(self.synthesizer.generate_constant_wave(self.__tone_freq["h"], 4))
            elif tone == 50:
                self.__waves.append(self.synthesizer.generate_constant_wave(self.__tone_freq["h"], 2))
            elif tone == 51:
                self.__waves.append(self.synthesizer.generate_constant_wave(self.__tone_freq["h"], 1))
            else:
                print("Tone in variation can not be generated.")
                exit(1)

    def play(self):
        player = Player()
        player.open_stream()
        for variation in self.__variations:
            self.__generate_waves(variation)
        self.__waves = np.concatenate(self.__waves)
        player.play_wave(self.__waves)

    def save(self, file):
        writer = Writer()
        for variation in self.__variations:
            self.__generate_waves(variation)
        self.__waves = np.concatenate(self.__waves)
        writer.write_wave(file, self.__waves)
