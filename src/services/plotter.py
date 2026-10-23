import matplotlib
from matplotlib import pyplot

matplotlib.use("QtAgg")


def plot_audio(data, sample_rate):
    # Audion aikamuodon kaavio
    time = [i / sample_rate for i in range(len(data))]

    pyplot.figure(figsize=(14, 6))
    pyplot.plot(time, data)

    pyplot.xlabel("Aika[s]")
    pyplot.ylabel("Amplitudi")
    pyplot.title("Audion aaltomuoto")
    pyplot.grid()

    pyplot.show()


def plot_fft(data, sample_rate):
    # Audion taajusmuodon kaavio
    n = len(data)

    magnitude = [abs(value) for value in data]

    frequencies = [i * sample_rate / n for i in range(n // 2)]

    pyplot.figure(figsize=(14, 6))
    pyplot.plot(frequencies, magnitude[: n // 2])

    pyplot.xlabel("Taajuus[Hz]")
    pyplot.ylabel("Voimakkuus")
    pyplot.title("Audion FFT")
    pyplot.grid()

    pyplot.show()
