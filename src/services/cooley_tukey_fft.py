import math
import cmath
import numpy

class Fourier:
    def __init__(self, audio_data):
        if len(audio_data) % 2 != 0:
            self.data = audio_data
            self.data = numpy.append(self.data, 0)
        else:
            self.data = audio_data

    def rad2ct(self, data):
        n = len(data)
        if n == 1:
            return data

        even = data[::2]
        odd = data[1::2]

        y0 = self.rad2ct(even)
        y1 = self.rad2ct(odd)

        w = cmath.exp(-2j * math.pi / n)
        wn = 1

        y = numpy.zeros(n, dtype=complex)

        for i in range(n//2):
            y[i] = y0[i] + (wn * y1[i])
            y[i + (n//2)] = y0[i] - (wn * y1[i])

            wn *= w

        return y

    def do_fft(self):
        fft_data = self.rad2ct(self.data)
        return fft_data
