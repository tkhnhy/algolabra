from services.plotter import plot_audio, plot_fft

class Cli:
    def get_source(self):
        print("Kirjoita polku audiotiedostoon jonka haluat analysoida:")
        #tässä esim. example_audio\sine_440Hz.wav
        audio_source = input()

        return audio_source

    def print_frequency(self, frequency):
        print(f"Voimakkain taajuus on {frequency}")

    def show_plots(self, original_data, new_data, sample_rate):
        plot_audio(original_data, sample_rate)
        plot_fft(new_data, sample_rate)
