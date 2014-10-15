import json
import time
import datetime

def moveOneWords(in_name):
 
    in_file = open(in_name,'r')
    lines = in_file.readlines()
    in_file.close()

    words = []

    for i in range(17):
        words.append([])

    for line in lines:

        line = line.rstrip()

        line_words = line.split()

        for i in range(17):
            if len(line_words) == i+1:
                words[i].append(line)
    
    out_name = "common/dict_versions/dict_v5.txt"
    out_file = open(out_name, 'w')
    for i in range(17):
        # j = i + 1
        # out_name = "common/n_word_phrases/%d_word.txt" % j
        # out_file = open(out_name, 'w')

        # for w in words[i]:
        #    out_file.write(w) #"%s\n" % w

        json.dump(words[i], out_file)
        json.dump('XYZZY', out_file)
        # out_file.close()
    out_file.close()

    return

def addWord(word, word_list):
    """
    Makes sure word_list has unique elements.
    """
    for item in word_list:
        if word == item:
            return

    word_list.append(word)
    return

if __name__ == "__main__":
    in_name = raw_input("Input file: ")
    #out_name = raw_input("Output file: ")
    ts1 = time.time()
    hr_ts1 = datetime.datetime.fromtimestamp(ts1).strftime('%Y-%m-%d %H:%M:%S')
    print "Processing started at %s" %hr_ts1
    moveOneWords(in_name)
    ts2 = time.time()
    hr_ts2 = datetime.datetime.fromtimestamp(ts2).strftime('%Y-%m-%d %H:%M:%S')
    print "Processing completed at %s" %hr_ts2
    print "Time elapsed (seconds): %f" %float(ts2-ts1)
