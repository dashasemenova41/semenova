import mcp4725_driver as mcp
import triangle as sg
import time

amplitude = 3
signal_frequency = 10
sampling_frequency = 1000

try:
    dac = mcp.MCP4725(amplitude)
        
    while True:
        normalized = sg.get_amplitude(signal_frequency, time.time())
        voltage = normalized * amplitude
            
        dac.set_voltage(voltage)
   
            


finally:
    dac.set_voltage(0)  
    dac.deinit()