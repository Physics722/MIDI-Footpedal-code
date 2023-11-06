import machine
from machine import Pin, ADC
import time

adcPedal = ADC(28)
pedalValue = 234
while True:
    if pedalValue != 765 #the adc reading subtract amount
        pedalValue = 4
        print(pedalValue)
    time.sleep(0.1)
