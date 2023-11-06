import time
import mido
from mido import Message
mido.set_backend('mido.backends.rtmidi')

try:
    outport  = mido.open_output('me', virtual='True')
except:
    print("Error: cannot connect to MIDI output")
    
inport = mido.open_input('Thomas', virtual='True')
outport = mido.open_output('Thomas', virtual="True")

print(outport)

import serial

# Configure the serial port
#numberPort = input("number port")
ser = serial.Serial('/dev/ttyACM0', 9600)  # Change '/dev/ttyUSB0' to the correct port
#print('/dev/ttyACM' + numberPort)

while True:
    # Read and print the serial data
    data = ser.readline().decode('utf-8')
    print(data, end='')
    #do stuff with the data
    msg = Message("pitchwheel", pitch = 8191)
    outport.send(msg)

