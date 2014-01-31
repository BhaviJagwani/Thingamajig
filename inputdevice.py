import pyaudio
import serial
import time
import wave
from array import array
from struct import pack
from sys import byteorder

class InputDevice:
    def __init__(self, serial):
        self.serial = serial

    """Read from RFID reader and return rfid if found"""
    def read(self):
        self.serial.flushInput()
        rfid = self.serial.readline()
        rfid = rfid.rstrip()
        return rfid

    """Record audio from mic, store to file and return file name"""
    def record(self):
        print "Recording"

        RATE = 44100
        FORMAT = pyaudio.paInt16
        THRESHOLD = 500
        CHUNK_SIZE = 1024

        p = pyaudio.PyAudio()

        stream = p.open(format=FORMAT, channels=1, rate=RATE,
                        input=True, output=True,
                        frames_per_buffer=CHUNK_SIZE)

        snd_started = False
        data = array('h')

        while True:
            snd_data = array('h', stream.read(CHUNK_SIZE))
            if byteorder == 'big': snd_data.byteswap()

            data.extend(snd_data)

            keypress = self.serial.read()
            self.serial.flushInput()
            print keypress
            if keypress == '0':
                break;

        self.serial.write('c')
        self.serial.flushInput()

        sample_width = p.get_sample_size(FORMAT)
        stream.stop_stream()
        stream.close()
        p.terminate()

        sound_file = str(int(time.time()))+".wav"
        path = "sounds/"+sound_file

        data = pack('<' + ('h'*len(data)), *data)

        wf = wave.open(path, 'wb')
        wf.setnchannels(1)
        wf.setsampwidth(sample_width)
        wf.setframerate(RATE)
        wf.writeframes(data)
        wf.close()

        print "Done recording"
        return sound_file
