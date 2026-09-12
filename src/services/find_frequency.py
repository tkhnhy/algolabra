from services.audio_handler import AudioHandler

class FrequencyFinder:
    def find_frequency(self, audio_source):
        audio_handler = AudioHandler(audio_source)
        audio_data = audio_handler.readfile()

        #Tähän väliin fft, palauta sen data kun valmis
        return audio_data