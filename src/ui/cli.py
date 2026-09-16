class Cli:
    def get_source(self):
        print("Kirjoita polku audiotiedostoon jonka haluat analysoida:")
        #tässä esim. example_audio\sine_440Hz.wav
        audio_source = input()
        
        return audio_source
     
    def print_frequency(self, frequency):
        print(f"Voimakkain taajuus on {frequency}")
        
        return
