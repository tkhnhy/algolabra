from services.audio_handler import AudioHandler

from services.cooley_tukey_fft import Fourier, do_inverse

import numpy

class FrequencyFinder:
    def find_frequency(self, audio_source):
        audio_handler = AudioHandler(audio_source)

        audio_data, sample_rate = audio_handler.readfile()

        original_data = audio_data.copy()

        fft = Fourier(audio_data)
        transformed = fft.do_fft()
        
        magnitude = numpy.abs(transformed)
        peak_index = numpy.argmax(magnitude)
        peak_frequency = peak_index * sample_rate / len(transformed)

<<<<<<< HEAD
        return transformed

    def inversefft(self, data):
        return do_inverse(data)
=======
       
        return original_data, transformed, sample_rate, peak_frequency
>>>>>>> main
