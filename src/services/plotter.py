from matplotlib import pyplot
import numpy

def plot_audio(data, sample_rate):

    time = numpy.arange(len(data)) / sample_rate

    pyplot.figure(figsize=(14, 6))
    pyplot.plot(time, data)

    pyplot.xlabel("Aika[s]")
    pyplot.ylabel("Amplitudi")
    pyplot.title("Audion aaltomuoto")
    pyplot.grid()

    pyplot.show()

def plot_fft(data, sample_rate):
    n = len(data)

    magnitude = numpy.abs(data)

    frequencies = numpy.arange(n // 2) * sample_rate / n

    pyplot.figure(figsize=(14, 6))
    pyplot.plot(frequencies, magnitude[:n // 2])

    pyplot.xlabel("Taajuus[Hz]")
    pyplot.ylabel("Voimakkuus")
    pyplot.title("Audion FFT")
    pyplot.grid()

    pyplot.show()
