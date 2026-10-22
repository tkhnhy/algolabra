import unittest
import pytest
import numpy
from src.services.cooley_tukey_fft import Fourier


def generate_random_data(n):
    return 2 * numpy.random.rand(n) - 1


@pytest.mark.performance
def test_fft_performance_n_256(benchmark):
    n = 256
    data = generate_random_data(n)
    fourier = Fourier(data)

    result = benchmark(fourier.do_fft)

    assert result.shape == (n,)
    
@pytest.mark.performance
def test_fft_performance_n_512(benchmark):
    n = 512
    data = generate_random_data(n)
    fourier = Fourier(data)

    result = benchmark(fourier.do_fft)

    assert result.shape == (n,)
    
@pytest.mark.performance
def test_fft_performance_n_1024(benchmark):
    n = 1024
    data = generate_random_data(n)
    fourier = Fourier(data)

    result = benchmark(fourier.do_fft)

    assert result.shape == (n,)
    
@pytest.mark.performance
def test_fft_performance_n_2048(benchmark):
    n = 2048
    data = generate_random_data(n)
    fourier = Fourier(data)

    result = benchmark(fourier.do_fft)

    assert result.shape == (n,)
    
@pytest.mark.performance
def test_fft_performance_n_4096(benchmark):
    n = 4096
    data = generate_random_data(n)
    fourier = Fourier(data)

    result = benchmark(fourier.do_fft)

    assert result.shape == (n,)