#!/usr/bin/python

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
