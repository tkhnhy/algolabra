from services.audio_handler import AudioHandler

from services.cooley_tukey_fft import Fourier

class FrequencyFinder:
    def find_frequency(self, audio_source):
        audio_handler = AudioHandler(audio_source)
        audio_data = audio_handler.readfile()

        fft = Fourier(audio_data)
        transformed = fft.do_fft()

        return transformed

    def inversefft(self, data):
        return fft.do_inverse(data)
