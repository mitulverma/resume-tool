import json
import time
import datetime

def removeQuotes(in_name, out_name):
 
    in_file = open(in_name,'r')
    lines = in_file.readlines()
    in_file.close()

    out_file = open(out_name, 'w')

    words = []

    for line in lines:
        new_word = ""

        # Remove quotes and decimal points (because they can be confused
        # with full stops).
        for c in line:
            if c != "\"":
                new_word+=c
        line = new_word
        
        addWord(line, words)


        # line_words = line.split()
        # if len(line_words) > 1:

        # for word in line_words:

        #     new_word = ""

        #     # Remove quotes and decimal points (because they can be confused
        #     # with full stops).
        #     for c in word:
        #         if c != "\"" and c != ".":
        #             new_word+=c
        #     word = new_word
            
        #     addWord(word, words)

    for w in words:
        out_file.write(w) #"%s\n" % w

    # json.dump(words, out_file)
    # out_file.close()

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
    out_name = raw_input("Output file: ")
    ts1 = time.time()
    hr_ts1 = datetime.datetime.fromtimestamp(ts1).strftime('%Y-%m-%d %H:%M:%S')
    print "Processing started at %s" %hr_ts1
    removeQuotes(in_name, out_name)
    ts2 = time.time()
    hr_ts2 = datetime.datetime.fromtimestamp(ts2).strftime('%Y-%m-%d %H:%M:%S')
    print "Processing completed at %s" %hr_ts2
    print "Time elapsed (seconds): %f" %float(ts2-ts1)
