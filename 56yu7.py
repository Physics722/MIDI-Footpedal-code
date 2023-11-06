import machine
from machine import Pin, ADC
import time

adcPedal = ADC(28)
pedalValue = 234
pedalReading = round(abs(adcPedal.read_u16()-64239)/10)
while True:
    if pedalValue != pedalReading: #the adc reading subtract amount
        if pedalReading < 4:
               pedalValue = 0
        elif pedalReading > 127:
            pedalValue = 127
        else:
            pedalValue = pedalReading
        print(pedalValue)
    time.sleep(0.1)
