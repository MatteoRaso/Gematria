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

#Gets every sentence that matches a certain gematria and saves it to a txt file.

def get_gematria_sentences(gematria):

    file_name = str(gematria) + '.txt'
    f = open("sentences.txt", 'r')
    g = open(file_name, 'w')

    cache = []

    for lines in f:
        try:
            string = lines.strip('\n')
            #We need to be careful here, because the sentence can
            #contain multiple instances of '---'
            string = string.split('---')
            #We need to format the test string to see if it's in cache
            test_string = ''.join(string).replace(string[-1], '')
            test_string = test_string.replace('\n', '')
            test_string = test_string.replace('\t', '')
            test_string = test_string.replace(' ', '')
            test_string = test_string.replace('\"', '')
            test_string = test_string.replace("'", "")
            #The last element in the list is the gematria
            if int(string[-1]) == gematria and test_string not in cache:
                #We want to make sure we don't repeat strings.
                cache.append(test_string)
                #We need to remove the gematria from the list and
                #convert the list into a string to write to the file.
                string.remove(string[-1])
                g.write(''.join(string) + '\n')

        except ValueError:
            continue

    f.close()
    g.close()
