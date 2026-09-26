import soundfile
import numpy

class AudioHandler:
    def __init__(self, audio_source):
        self.audio_source = audio_source
        self.original_length = 0
    def readfile(self):
        data, sample_rate = soundfile.read(self.audio_source)

        self.sample_rate = sample_rate

        if data.ndim == 2:
            mono_data = numpy.mean(data, axis=1)
        else:
            mono_data = data

        self.original_length = len(mono_data)
        return (mono_data, sample_rate)

    def writefile(self, data):
        soundfile.write("output_audio/output.wav",
        data[:self.original_length], self.sample_rate)
