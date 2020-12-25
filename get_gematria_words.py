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

#Gets every word that matches the gematria and writes it to a file.

def get_gematria_words(gematria, swear_words = False):
    if swear_words:
        f = open("every_word_plus_gematria.txt", 'r')

    else:
        f = open("every_clean_word_plus_gematria.txt", 'r')

    g = open(str(gematria) + ".txt", 'w')

    for line in f:
        #We need a try-catch because of the copyright info.
        try:
            num = line.split(',')[1]
            num = num.replace('\n', '')
            if int(num) == gematria:
                g.write(line)

        except:
            continue

    f.close()
    g.close()
