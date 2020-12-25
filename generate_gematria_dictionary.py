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

#Takes in our massive text file of english words and generates a csv
#of every word and its gematria.

from calculate import *

def generate_gematria_dictionary():

    f = open("every_word.txt", 'r')
    g = open("every_word_plus_gematria.txt", 'w')

    #Copyright info has to be written in every file.
    g.write("Copyright 2020 Matteo Raso\n")
    g.write("This file is part of Gematria.\n")
    g.write("Gematria is free software: you can redistribute it and/or modify\n")
    g.write("it under the terms of the GNU General Public License as published by\n")
    g.write("the Free Software Foundation, either version 3 of the License, or\n")
    g.write("(at your option) any later version.\n")
    g.write("\n")
    g.write("Gematria is distributed in the hope that it will be useful,\n")
    g.write("but WITHOUT ANY WARRANTY; without even the implied warranty of\n")
    g.write("MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the\n")
    g.write("GNU General Public License for more details.\n")
    g.write("\n")
    g.write("You should have received a copy of the GNU General Public License\n")
    g.write("along with Gematria.  If not, see <https://www.gnu.org/licenses/>.\n\n") 

    i = 1

    for line in f:
        #To avoid calculating the copyright info.
        if i > 15:
            formatted_line = line.replace('\n', '')
            string = formatted_line + "," + str(calculate(formatted_line)) + '\n'
            g.write(string)

        i += 1

    f.close()
    g.close()

generate_gematria_dictionary()
