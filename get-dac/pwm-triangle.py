import pwm_dac as pwm
import triangle as sg
import time

amplitude = 3
signal_frequency = 1000
sampling_frequency = 100

try:
    dac = pwm.PWM_DAC(12, 6000, 3, True)
        
    while True:
        normalized = sg.get_amplitude(signal_frequency, time.time())
        voltage = normalized * amplitude
            
        dac.set_voltage(voltage)
   

            


finally:
    dac.set_voltage(0)  
    dac.deinit()
    
