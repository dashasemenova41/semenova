import r2r_dac as r2r
import triangle as sg
import time

amplitude = 2
signal_frequency = 100
sampling_frequency = 500

try:
    dac = r2r.R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], amplitude, True)
        
    while True:
        normalized = sg.get_amplitude(signal_frequency, time.time())
        voltage = normalized * amplitude
            
        dac.set_voltage(voltage)
   

            


finally:
    dac.set_voltage(0)  
    dac.deinit()
    
