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

msg = Message('note_on', note=64)

time.sleep(10)
outport.send(msg)

time.sleep(8)
outport.close()
