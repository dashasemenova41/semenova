import time


def get_amplitude(freq, time):
    period = 1/freq
    time_norm = (time % period)/period
    if time_norm < 0.5:
        return 2 * time_norm
    return 2 * (1 - time_norm)

def wait_for_sampling_period(sampling_frequency):
    period = 1.0 / sampling_frequency
    time.sleep(period)
