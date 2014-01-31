import serial
from datastore import *
from inputdevice import *

ser = serial.Serial('/dev/ttyUSB1', 9600)

ds = DataStore()
ip = InputDevice(ser)

while True:
    rfid = ip.read()
    print "Detected "+rfid


    if rfid[0] == '0':
        print "Try again"
        ser.flushInput()
    else:
        print "Press button to record"
        recorded = False
        while not recorded:
            keypress = ser.read()
            if keypress == '1':
                sound_file = ip.record()
                ser.flushInput()
                ds.set_sound_file_for_rfid(sound_file, rfid)
                print "Associated "+sound_file+" with RFID "+rfid
                recorded = True