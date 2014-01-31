import csv

class DataStore:
    """Load associations from file when initialized"""
    def __init__(self):
        self.now_playing = []
        self.rfid_sounds_dict = {}
        self.file_sounds_dict = {}

        for key, val in csv.reader(open("rfid_sounds.csv")):
            self.rfid_sounds_dict[key] = val

    def get_sound_file_from_rfid(self, rfid):
        for key, val in csv.reader(open("rfid_sounds.csv")):
            self.rfid_sounds_dict[key] = val

        return self.rfid_sounds_dict[rfid]

    def set_sound_file_for_rfid(self, sound_file, rfid):
        self.rfid_sounds_dict[rfid] = sound_file

        w = csv.writer(open("rfid_sounds.csv", "w"))
        for key in self.rfid_sounds_dict:
            w.writerow([key, self.rfid_sounds_dict[key]])

    def add_sound_file_to_now_playing(self, sound_file):
        self.now_playing.append(sound_file)

    def search_sound_file_in_now_playing(self, sound_file):
        return sound_file in self.now_playing

    def remove_sound_file_from_now_playing(self, sound_file):
        if sound_file in self.now_playing: self.now_playing.remove(sound_file)

    def get_sound_playing_for_sound_file(self, sound_file):
        return self.file_sounds_dict[sound_file]

    def set_sound_playing_for_sound_file(self, sound, sound_file):
        self.file_sounds_dict[sound_file] = sound

    def reset_sound_playing_for_sound_file(self, sound_file):
        self.file_sounds_dict[sound_file] = None

# ds = DataStore()

# ds.set_sound_file_for_rfid("qwerty.wav", "123456")
# ds.set_sound_file_for_rfid("qwerty.wav", "123456\n".rstrip())