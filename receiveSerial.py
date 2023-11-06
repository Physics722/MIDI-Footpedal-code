import serial

# Configure the serial port
numberPort = input("number port")
ser = serial.Serial('/dev/ttyACM' + numberPort, 9600)  # Change '/dev/ttyUSB0' to the correct port
#print('/dev/ttyACM' + numberPort)

while True:
    # Read and print the serial data
    data = ser.readline().decode('utf-8')
    print(data, end='')
    #do stuff with the data
