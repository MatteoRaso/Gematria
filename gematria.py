#!/usr/bin/python

#Copyright 2020 Matteo Raso
#This file is part of Gematria.
#
#    Gematria is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Gematria is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with Gematria.  If not, see <https://www.gnu.org/licenses/>.

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
    print("-b           Boring license info for lawyers and nerds.")

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

elif sys.argv[1] == '-b':
    print("Copyright 2020 Matteo Raso\n")
    print("Gematria is free software: you can redistribute it and/or modify\n")
    print("it under the terms of the GNU General Public License as published by\n")
    print("the Free Software Foundation, either version 3 of the License, or\n")
    print("(at your option) any later version.\n")
    print("\n")
    print("Gematria is distributed in the hope that it will be useful,\n")
    print("but WITHOUT ANY WARRANTY; without even the implied warranty of\n")
    print("MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the\n")
    print("GNU General Public License for more details.\n")
    print("\n")
    print("You should have received a copy of the GNU General Public License\n")
    print("along with Gematria.  If not, see <https://www.gnu.org/licenses/>.\n\n")
