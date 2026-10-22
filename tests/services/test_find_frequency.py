import unittest
import numpy
from unittest.mock import patch

from src.services.find_frequency import FrequencyFinder

class TestFrequencyFinder(unittest.TestCase):
    @patch("src.services.find_frequency.AudioHandler")
    def test_find_frequency(self, mock_audio_handler):
        test_sample_rate = 44100
        audio_data = numpy.load("testdata/sine_440Hz_padded_data.npy")
        
        mock_audio_handler.return_value.readfile.return_value = (audio_data, test_sample_rate)
        
        finder = FrequencyFinder("testing.wav")
        
        original_data, transformed, sample_rate, peak_frequency = (finder.find_frequency())
        
        self.assertEqual(440, round(peak_frequency))