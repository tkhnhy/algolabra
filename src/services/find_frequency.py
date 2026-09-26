from services.audio_handler import AudioHandler

from services.cooley_tukey_fft import Fourier, do_inverse

import numpy

class FrequencyFinder:
    def __init__(self, audio_source):
        self.audio_handler = AudioHandler(audio_source)
    def find_frequency(self):
        
        audio_data, sample_rate = self.audio_handler.readfile()

        original_data = audio_data.copy()

        fft = Fourier(audio_data)
        transformed = fft.do_fft()
        
        magnitude = numpy.abs(transformed)
        peak_index = numpy.argmax(magnitude)
        peak_frequency = peak_index * sample_rate / len(transformed)

       
        return original_data, transformed, sample_rate, peak_frequency

    def invert_and_write(self, data):
        to_write = numpy.real(do_inverse(data))
        self.audio_handler.writefile(to_write)