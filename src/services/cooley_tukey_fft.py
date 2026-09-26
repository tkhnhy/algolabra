import math
import cmath
import numpy

class Fourier:
    def __init__(self, audio_data):
        n = len(audio_data)
        next_power_2 = 1 << (n - 1).bit_length()

        self.data = numpy.pad(audio_data,(0, next_power_2 - n))

    def rad2ct(self, data):
        n = len(data)
        if n == 1:
            return data

        even = data[::2]
        odd = data[1::2]

        y0 = self.rad2ct(even)
        y1 = self.rad2ct(odd)

        wn = cmath.exp(-2j * math.pi / n)
        w = 1

        y = numpy.zeros(n, dtype=complex)

        for i in range(n//2):
            y[i] = y0[i] + (w * y1[i])
            y[i + (n//2)] = y0[i] - (w * y1[i])

            w *= wn

        return y

    def do_fft(self):
        return self.rad2ct(self.data)

def inverserad2ct(data):
    n = len(data)
    if n == 1:
        return data

    even = data[::2]
    odd = data[1::2]

    y0 = inverserad2ct(even)
    y1 = inverserad2ct(odd)

    wn = cmath.exp(2j * math.pi / n)
    w = 1

    y = numpy.zeros(n, dtype=complex)

    for i in range(n//2):
        y[i] = y0[i] + (w * y1[i])
        y[i + (n//2)] = y0[i] - (w * y1[i])

        w *= wn

    return y

def do_inverse(data):
    n = len(data)
    return (1/ n) * inverserad2ct(data)
