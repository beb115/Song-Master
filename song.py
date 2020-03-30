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
        while('' in self.song):
            self.song.remove('')

        print(choice(self.song))

#makeSong looks awful, clean it up
def makeSong(artist):
    if artist != None:
        pass
    else:
        artist = input("What Band?\n")
    numOfLines = input("How many lines would you like?\n")
    breakPoint = input("Where would you like the break point?\n")
    print("")
    for i in range(int(numOfLines)):  # Line needs to be redone, to much conversion
        if i % int(breakPoint) == 0 and i != 0:
            print("")
            Lyric(artist)
        else:
            Lyric(artist)
