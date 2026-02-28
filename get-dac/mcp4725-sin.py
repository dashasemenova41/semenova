import mcp4725_driver as mcp
import signal_generator as sg
import time

amplitude = 3
signal_frequency = 10
sampling_frequency = 100

try:
    dac = mcp.MCP4725(amplitude)
        
    while True:
        normalized = sg.get_sin_wave_amplitude(signal_frequency, time.time())
        voltage = normalized * amplitude
            
        dac.set_voltage(voltage)
   
        sg.wait_for_sampling_period(sampling_frequency)
            


finally:
    dac.set_voltage(0)  
    dac.deinit()