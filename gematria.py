#!/usr/bin/python

#The main function, where the user calls all the other functions.

import sys

from calculate import *
from generate_clean_gematria_dictionary import *
from generate_gematria_dictionary import *
from get_gematria_sentences import *
from get_gematria_words import *

if sys.argv[1] == '-h':
    print("-c           Gets the gematria of a string.")
    print("-d           Generates a dictionary of words and their gematria.")
    print("-dc          Same as '-d', but with no swear words.")
    print("-w           Gets every word with a user-given gematria. The user may optionally input a boolean to determine whether swear words are allowed.")
    print("-s           Gets every sentence with a user-given gematria.")
    print("-h           Brings up this help page.")

elif sys.argv[1] == '-c':
   gem = calculate(sys.argv[2])
   print("The gematria of " + sys.argv[2] + " is " + str(gem) + '.')

elif sys.argv[1] == '-d':
    generate_gematria_dictionary()

elif sys.argv[1] == '-dc':
    generate_clean_gematria_dictionary()

elif sys.argv[1] == '-w':
        try:
            get_gematria_words(int(sys.argv[2]), sys.argv[3])

        #The user might not input the boolean.
        except:
            get_gematria_words(int(sys.argv[2]))

        print(sys.argv[2] + ".txt has been successfully written.")

elif sys.argv[1] == '-s':
    get_gematria_sentences(int(sys.argv[2]))
