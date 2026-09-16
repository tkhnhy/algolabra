import soundfile, numpy

class AudioHandler:
    def __init__(self, audio_source):
        self.audio_source = audio_source
        
    def readfile(self):
        data, sample_rate = soundfile.read(self.audio_source)

        if data.ndim == 2:
            mono_data = np.mean(data, axis=1)
        else:
            mono_data = data

        return (mono_data, sample_rate)
