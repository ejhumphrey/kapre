import pytest

import kapre.time_frequency


def test_Spectrogram___init__():
    layer = kapre.time_frequency.Spectrogram(
        n_dft=512, n_hop=256, padding='valid', power_spectrogram=2.0,
        return_decibel_spectrogram=False, trainable_kernel=False,
        image_data_format='default')
    assert layer is not None


def test_Spectrogram_build():
    pass


def test_Spectrogram_compute_output_shape():
    pass


def test_Spectrogram_call():
    pass


def test_Spectrogram_get_config():
    pass


def test_Spectrogram__spectrogram_mono():
    pass


def test_Melspectrogram___init__():
    pass


def test_Melspectrogram_build():
    layer = kapre.time_frequency.Melspectrogram(
        sr=22050, n_mels=128, fmin=0.0, fmax=None,
        power_melgram=1.0, return_decibel_melgram=False,
        trainable_fb=False)
    assert layer is not None


def test_Melspectrogram_compute_output_shape():
    pass


def test_Melspectrogram_call():
    pass


def test_Melspectrogram_get_config():
    pass
