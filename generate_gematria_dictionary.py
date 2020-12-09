#!/usr/bin/python

#Takes in our massive text file of english words and generates a csv
#of every word and its gematria.

from calculate import *

def generate_gematria_dictionary():

    f = open("every_word.txt", 'r')
    g = open("every_word_plus_gematria.txt", 'w')

    for line in f:
        formatted_line = line.replace('\n', '')
        string = formatted_line + "," + str(calculate(formatted_line)) + '\n'
        g.write(string)

    f.close()
    g.close()

generate_gematria_dictionary()
