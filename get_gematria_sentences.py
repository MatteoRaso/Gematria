#!/usr/bin/python

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
