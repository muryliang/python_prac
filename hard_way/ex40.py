# -*- coding: utf-8 -*-

class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self) :
        for line in self.lyrics:
            print line

    def shout(self):
        print 'haha'


fist = ["Happy Brithday to you",
        "I don't want to get sued",
        "So I'l stop right there"]

second = ["They rally around tha family",
                        "With pockets full of shells"]

happy_bday = Song(fist)
bulls_on_parade = Song(second)


happy_bday.sing_me_a_song()
happy_bday.shout()
bulls_on_parade.sing_me_a_song()
