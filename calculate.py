#!/usr/bin/python

#Gets the gematria of a given phrase.

#Our conversion chart

codex = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7,
         'h': 8, 'i': 9, 'j': 10, 'k': 20, 'l': 30, 'm': 40, 'n': 50,
         'o': 60, 'p': 70, 'q': 80, 'r': 90, 's': 100, 't': 200, 'u': 300,
         'v': 400, 'w': 500, 'x': 600, 'y': 700, 'z': 800}

def calculate(string):
    #This just makes it easy to read from the dictionary.
    string = string.lower()
    gematria = 0
    for char in string:
        try:
            gematria += codex[char]

        #Skips over special characters and whitespace.
        except KeyError:
            pass

    return gematria
