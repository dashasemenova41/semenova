import pwm_dac as pwm
import signal_generator as sg
import time

amplitude = 3
signal_frequency = 50
sampling_frequency = 1000

try:
    dac = pwm.PWM_DAC(12, 500, 3, True)
        
    while True:
        normalized = sg.get_sin_wave_amplitude(signal_frequency, time.time())
        voltage = normalized * amplitude
            
        dac.set_voltage(voltage)
   
        sg.wait_for_sampling_period(sampling_frequency)
            


finally:
    dac.set_voltage(0)  
    dac.deinit()
    