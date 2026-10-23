import unittest
import numpy
from src.services.cooley_tukey_fft import Fourier, do_inverse


class TestFourier(unittest.TestCase):
    def assert_lists_almost_equal(self, result, expected, round_exp: bool):
        self.assertEqual(len(result), len(expected))

        rounded = [complex(round(x.real, 2), round(x.imag, 2)) for x in result]

        if round_exp:
            rounded_expected = [complex(round(x.real, 2), round(x.imag, 2)) for x in expected]
            self.assertEqual(rounded, rounded_expected)
        else:
            self.assertEqual(rounded, expected)

    def test_fft(self):
        data = [1, 2, 3, 4]

        fourier = Fourier(data)

        expected = [10 + 0j, -2 + 2j, -2 + 0j, -2 - 2j]
        result = fourier.do_fft()

        self.assert_lists_almost_equal(result, expected, False)

    def test_fft_non_power_of_2(self):
        data = [1, 2, 3]
        data_padded = [1, 2, 3, 0]

        fourier = Fourier(data)

        expected = numpy.fft.fft(data_padded).tolist()
        result = fourier.do_fft()

        self.assert_lists_almost_equal(result, expected, True)

    def test_do_inverse(self):
        data = [10 + 0j, -2 + 2j, -2 + 0j, -2 - 2j]

        expected = [1 + 0j, 2 + 0j, 3 + 0j, 4 + 0j]
        result = do_inverse(data)

        self.assert_lists_almost_equal(result, expected, False)

    def test_data_is_empty(self):
        data = []

        fourier = Fourier(data)
        result = fourier.do_fft()

        expected = []

        self.assert_lists_almost_equal(result, expected, False)

    def test_all_single_entry(self):
        data = [1]

        fourier = Fourier(data)

        expected = [1]
        result = fourier.do_fft()

        self.assert_lists_almost_equal(result, expected, False)

    def test_all_zeroes(self):
        data = [0, 0, 0, 0]

        fourier = Fourier(data)

        expected = [0, 0, 0, 0]
        result = fourier.do_fft()

        self.assert_lists_almost_equal(result, expected, False)

    def test_all_ones(self):
        data = [1, 1, 1, 1]

        fourier = Fourier(data)

        expected = [4, 0, 0, 0]
        result = fourier.do_fft()

        self.assert_lists_almost_equal(result, expected, False)

    def test_all_alternate_one_minusone(self):
        data = [1, -1, 1, -1]

        fourier = Fourier(data)

        expected = [0, 0, 4, 0]
        result = fourier.do_fft()

        self.assert_lists_almost_equal(result, expected, False)

    def test_compare_to_numpy_on_real_data(self):
        data = numpy.load("testdata/sine_440Hz_padded_data.npy").tolist()

        expected = numpy.fft.fft(data).tolist()

        fourier = Fourier(data)
        result = fourier.do_fft()

        self.assert_lists_almost_equal(result, expected, True)

    def test_compare_to_numpy_2_different_volume_sine(self):
        # Sovellus ei aikaisemmin toiminut oikein tällä äänitiedostolla
        data = numpy.load("testdata/C4loudA4quiet_padded_data.npy").tolist()

        expected = numpy.fft.fft(data).tolist()

        fourier = Fourier(data)
        result = fourier.do_fft()

        self.assert_lists_almost_equal(result, expected, True)

    def test_original_data_retained_after_both_fft_ifft(self):
        data = numpy.load("testdata/sine_440Hz_padded_data.npy").tolist()

        fourier = Fourier(data)
        transformed = fourier.do_fft()

        result = do_inverse(transformed)

        self.assert_lists_almost_equal(result, data, True)
