import lyricsgenius
import os
from song import makeSong

os.getcwd()


def makeBuild():
    band = input("Welcome\nEnter Band Name:")
    genius = lyricsgenius.Genius(
        "oHsqgqThDrBdxCFfgveI8FTAaWH0X8OB1NMYYcmhakjKPxLb--1AaseXTLd-CLEf", remove_section_headers=True)
    artist = genius.search_artist(band, max_songs=15, get_full_info=False)

    print(artist.songs)

    artist.save_lyrics()
    newSong(artist.name)


def newSong(artist):
    print("Would you like to make a song now?")
    ynInput = input("y/n... ")
    if (ynInput.lower() == "y"):
        makeSong(artist)
    elif (ynInput.lower() == "n"):
        pass
    else:
        print("Please use Y or N")
        newSong(artist)
