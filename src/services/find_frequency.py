import numpy

from services.audio_handler import AudioHandler

from services.cooley_tukey_fft import Fourier, do_inverse

class FrequencyFinder:
    def __init__(self, audio_source):
        self.audio_handler = AudioHandler(audio_source)
        self.peak_index = 0;
        self.peak_frequency = 0;

    def find_frequency(self):

        audio_data, sample_rate = self.audio_handler.readfile()

        original_data = audio_data.copy()

        fft = Fourier(audio_data)
        transformed = fft.do_fft()


        # Lasketaan fft:n tuottamien kompleksilukujen voimakkuudet ja haetaan niistä voimakkaimman taajuus
        magnitude = numpy.abs(transformed)
        self.peak_index = numpy.argmax(magnitude)
        self.peak_frequency = self.peak_index * sample_rate / len(transformed)


        return original_data, transformed, sample_rate, self.peak_frequency

    def invert_and_write(self, data):

        filtered = numpy.zeros_like(data)

        filtered[self.peak_index] = data[self.peak_index]
        to_write = numpy.real(do_inverse(filtered))
        self.audio_handler.writefile(to_write)
