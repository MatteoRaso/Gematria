#!/usr/bin/python

#Gets every word that matches the gematria and writes it to a file.

def get_gematria_words(gematria, swear_words = False):
    if swear_words:
        f = open("every_word_plus_gematria.txt", 'r')

    else:
        f = open("every_clean_word_plus_gematria.txt", 'r')

    g = open(str(gematria) + ".txt", 'w')

    for line in f:
        num = line.split(',')[1]
        num = num.replace('/n', '')
        if int(num) == gematria:
            g.write(line)

    f.close()
    g.close()
