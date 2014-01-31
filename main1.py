import serial
from datastore import *
from primaryinterface import *

ser = serial.Serial('/dev/ttyUSB0', 9600)

ds = DataStore()
pi = PrimaryInterface(ser)

while True:
    rfid = pi.read()

    sound_file = ''
    try:
        sound_file = ds.get_sound_file_from_rfid(rfid)
    except KeyError:
        pass

    if ds.search_sound_file_in_now_playing(sound_file):
        sound = ds.get_sound_playing_for_sound_file(sound_file)

        pi.stop(sound)
        ds.remove_sound_file_from_now_playing(sound_file)
        print "Stopped "+sound_file
    else:
        sound = pi.play(sound_file)

        ds.add_sound_file_to_now_playing(sound_file)
        ds.set_sound_playing_for_sound_file(sound, sound_file)
        print "Played "+sound_file