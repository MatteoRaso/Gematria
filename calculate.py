#!/usr/bin/python

#Copyright 2020 Matteo Raso
#This file is part of Gematria.
#
#   Gematria is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or(at your option) any later version.
#
#   Gematria is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#
#along with Gematria.  If not, see <https://www.gnu.org/licenses/>.

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
