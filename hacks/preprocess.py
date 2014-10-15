import json

def preprocess(in_name, out_name):
 
    in_file = open(in_name,'r')
    lines = in_file.readlines()
    in_file.close()

    out_file = open(out_name, 'w')

    words = []

    for line in lines:
        line_words = line.split()
        for word in line_words:

            new_word = ""

            # Remove quotes and decimal points (because they can be confused
            # with full stops).
            for c in word:
                if c != "\"" and c != ".":
                    new_word+=c
            word = new_word
            
            addWord(word, words)

    # for w in words:
    #     out_file.write("%s\n" % w)

    json.dump(words, out_file)
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
    out_name = raw_input("Output file: ")
    #min_freq = raw_input("Frequency threshold of keywords: ")
    preprocess(in_name, out_name)
