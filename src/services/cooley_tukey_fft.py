import numpy, math, cmath

class Fourier:
    def __init__(self, audio_data):
        self.sample_rate = audio_data[1]

        if len(audio_data[0]) % 2 != 0:
            self.data = audio_data[0]
            self.data = numpy.append(self.data, 0)
        else:
            self.data = audio_data[0]

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
            y[i] = y0[i] + (w * y1[i])
            y[i + (n//2)] = y0[i] - (w * y1[i])

            wn *= w

        return y

    def inverserad2ct(self, data):
        n = len(data)
        if n == 1:
            return data

        even = data[::2]
        odd = data[1::2]

        y0 = self.inverserad2ct(even)
        y1 = self.inverserad2ct(odd)

        w = cmath.exp(2j * math.pi / n)
        wn = 1

        y = numpy.zeros(n, dtype=complex)

        for i in range(n//2):
            y[i] = y0[i] + (w * y1[i])
            y[i + (n//2)] = y0[i] - (w * y1[i])

            wn *= w

        return y

    def do_fft(self):
        return self.rad2ct(self.data)

    def do_inverse(self, data):
        n = len(data)
        return (1/ n) * self.inverserad2ct(data)
