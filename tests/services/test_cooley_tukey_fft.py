import unittest
import numpy
from src.services.cooley_tukey_fft import Fourier, do_inverse

class TestFourier(unittest.TestCase):
    def test_fft(self):
        data = numpy.array([1, 2, 3, 4])

        fourier = Fourier(data)

        expected = numpy.array([10+0j, -2+2j, -2+0j, -2-2j])
        result = fourier.do_fft()

        numpy.testing.assert_almost_equal(result, expected)

    def test_do_inverse(self):
        data = numpy.array([10+0j, -2+2j, -2+0j, -2-2j])

        expected = numpy.array([1+0j, 2+0j, 3+0j, 4+0j])

        result = do_inverse(data)

        numpy.testing.assert_almost_equal(result, expected)

    def test_compare_to_numpy_on_real_data(self):
        data = numpy.load("testdata/sine_440Hz_padded_data.npy")

        expected = numpy.fft.fft(data)

        fourier = Fourier(data)
        result = fourier.do_fft()

        numpy.testing.assert_almost_equal(result, expected)
