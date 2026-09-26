import soundfile
import numpy

class AudioHandler:
    def __init__(self, audio_source):
        self.audio_source = audio_source
<<<<<<< HEAD
        self.sample_rate = 0
        
=======

>>>>>>> main
    def readfile(self):
        data, sample_rate = soundfile.read(self.audio_source)

        self.sample_rate = sample_rate

        if data.ndim == 2:
            mono_data = numpy.mean(data, axis=1)
        else:
            mono_data = data

        return (mono_data, sample_rate)

    def writefile(self, data):
        soundfile.write(f"isolated_{self.audio_source}", data, self.sample_rate)
