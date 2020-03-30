import json
import pandas as pd
from pandas.io.json import json_normalize
from random import choice, randint


class Lyric:
    def __init__(self, artist):
        self.randSong = randint(0, 14)
        with open('Lyrics_' + artist.replace(" ", "") + '.json') as json_data:
            self.data = json.load(json_data)

        self.df = pd.DataFrame(self.data['songs'])
        self.song = self.df['lyrics'][self.randSong].splitlines()

        print(choice(self.song))


def makeSong(artist):
    if artist != None:
        pass
    else:
        artist = input("What Band?\n")
    numOfLines = input("How many lines would you like?\n")

    for i in range(int(numOfLines)):  # Line needs to be redone, to much conversion
        Lyric(artist)
