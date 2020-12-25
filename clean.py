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

#Takes every_word.txt and filters out the swears

bad_words = ["nigge", "shit", "cunt", "faggot", "gook", "kike", "fuck"]

def clean():
    f = open("every_word.txt", 'r')
    g = open("every_clean_word.txt", 'w')

    for line in f:
        remove = False
        for swear in bad_words:
            if line.find(swear) != -1:
                remove = True
                break

        if not remove:
            g.write(line)

    f.close()
    g.close()

clean()
