import numpy
import time
import math

def get_sin_wave_amplitude(freq, time):
    sinus = math.sin(2 * math.pi * freq * time)
    sin_up = sinus + 1
    normal = sin_up / 2

    return normal

def wait_for_sampling_period(sampling_frequency):
    period = 1.0 / sampling_frequency
    time.sleep(period)
