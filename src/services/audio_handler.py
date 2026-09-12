import soundfile, numpy

class AudioHandler:
    def __init__(self, audio_source):
        self.audio_source = audio_source
        
    def readfile(self):
        data, sample_rate = soundfile.read(self.audio_source)
        return (data, sample_rate)