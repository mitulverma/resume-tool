from common import stopwords, dictionary
import time
import datetime

def wordCount(file_name, min_freq, skill_flag):
    """
    Prints keywords used in order of maximum frequency of occurence in resume.
    The threshold frequency is described in min_freq.
    The skill_flag enables or disables filtering from the skills dictionary.
    """

    ## Read in file.
    resume = open(file_name,'r')
    lines = resume.readlines()
    resume.close()

    ## Construct a list that contains each word in the resume converted to 
    ## lowercase.
    words = []
    for line in lines:
        line_words = line.split()

        for word in line_words:

            # Remove trailing punctuation characters. If word is only one
            # punctuation character, leave it be. This accounts for '&' used
            # as the word 'and.' I can't think of any other cases, though, and
            # it may be useful to just ignore '&' specifcally instead of all
            # punctuation characters that appear as words.
            if len(word)!=1 and not word[-1].isalpha() and not word[-1].isdigit():
                word = word[0:-1]

            word = word.lower()

            words.append(word)


    ## Make five-or-fewer-word phrases using words list.

    # two_word_phrases = []
    # for i in range(len(words) - 1):
    #     phrase = words[i] + ' ' + words[i+1]
    #     two_word_phrases.append(phrase)

    # three_word_phrases = []
    # for i in range(len(words) - 2):
    #     phrase = words[i] + ' ' + words[i+1] + ' ' + words[i+2]
    #     three_word_phrases.append(phrase)

    # four_word_phrases = []
    # for i in range(len(words) - 3):
    #     phrase = words[i] + ' ' + words[i+1] + ' ' + words[i+2] + ' ' + \
    #              words[i+3]
    #     four_word_phrases.append(phrase)

    # five_word_phrases = []
    # for i in range(len(words) - 4):
    #     phrase = words[i] + ' ' + words[i+1] + ' ' + words[i+2] + ' ' + \
    #              words[i+3] + ' ' + words[i+4]
    #     five_word_phrases.append(phrase)

    five_or_fewer_word_phrases = fiveOrFewerWordPhrases(words)


    ## FIXME: Check for dictionary flag??? Find out if necessary!

    ## Populate output with one- thru five-word phrases

    # Done this way because there are many more dictionary entries than 
    # words in a typical resume.
    output = []

    for i in range(len(five_or_fewer_word_phrases)):
        for phrase in five_or_fewer_word_phrases[i]:
            if phrase in dictionary.five_or_fewer_word_phrases[i]:
                addWord(phrase, output)


    # for phrase in words:
    #     if phrase in dictionary.one_word_phrases:
    #         addWord(phrase, output)

    # for phrase in two_word_phrases:
    #     if phrase in dictionary.two_word_phrases:
    #         addWord(phrase, output)

    # for phrase in three_word_phrases:
    #     if phrase in dictionary.three_word_phrases:
    #         addWord(phrase, output)

    # for phrase in four_word_phrases:
    #     if phrase in dictionary.four_word_phrases:
    #         addWord(phrase, output)

    # for phrase in five_word_phrases:
    #     if phrase in dictionary.five_word_phrases:
    #         addWord(phrase, output)

    
    # Done this way because there are fewer dictionary entries >5 words than
    # words in a typical resume.

    # Create string of entire resume to search of >5-word phrases
    full_resume = ''
    for word in words:
        full_resume += word
        full_resume += ' '

    # Remark: there are no fifteen or sixteen word phrases in the provided
    #         dictionary.

    ## Populate output with >5-word phrases
    for phrase_list in dictionary.six_or_more_word_phrases:            
        for phrase in phrase_list:
            if phrase in full_resume:
                addWord(phrase, output)


            # if word not in stopwords.stopwords:
            #     word = removePunctuation(word)
            #     if word != "":
            #         if skill_flag != 'y':
            #             addWord(word, words)
            #         else:
            #             if word in dictionary.dictionary:
            #                 addWord(word, words)
                            # build n-word phrases by appending word + " " + word+1 + ... to
                            # lists one_word_phrases, two_word_phrases, etc

    output.sort(key = lambda x: x[1], reverse = True)
    # output.sort(key = lambda x: len(x[0]), reverse = True)

    count = 0

    for item in output:
        if item[1] >= min_freq:
            print item
            count +=1

    print count

    return

### DEFUNCT ###
# def removePunctuation(word):
#     """
#     Removes all non-alphabetical and non-numerical characters from word.
#     """

#     if not word[-1].isalpha() or not word[-1].isdigit():
#         word = word[0:-1]

#     new_word = ""
#     for letter in word:
#         # if letter.isalpha() or letter.isdigit() or letter == " ":
#             new_word += letter

#     return new_word

def fiveOrFewerWordPhrases(words):
    """
    """
    two_word_phrases = []
    for i in range(len(words) - 1):
        phrase = words[i] + ' ' + words[i+1]
        two_word_phrases.append(phrase)

    three_word_phrases = []
    for i in range(len(words) - 2):
        phrase = words[i] + ' ' + words[i+1] + ' ' + words[i+2]
        three_word_phrases.append(phrase)

    four_word_phrases = []
    for i in range(len(words) - 3):
        phrase = words[i] + ' ' + words[i+1] + ' ' + words[i+2] + ' ' + \
                 words[i+3]
        four_word_phrases.append(phrase)

    five_word_phrases = []
    for i in range(len(words) - 4):
        phrase = words[i] + ' ' + words[i+1] + ' ' + words[i+2] + ' ' + \
                 words[i+3] + ' ' + words[i+4]
        five_word_phrases.append(phrase)

    five_or_fewer_word_phrases = [words, two_word_phrases, three_word_phrases,
                                  four_word_phrases, five_word_phrases]

    return five_or_fewer_word_phrases


def addWord(word, word_list):
    """
    If an instance of word is present in word_list, addWord only increments its
    count/frequency. Else, it appends word onto word_list with count 1.
    """
    for item in word_list:
        if word == item[0]:
            item[1]+=1
            return

    word_list.append([word,1])
    return


if __name__ == "__main__":
    file_name = raw_input("Path to text file: ")
    min_freq = int(raw_input("Minimum frequency of keywords: "))
    skill_flag = raw_input(
        "Enter \'y\' if you want to filter keywords from skills dictionary: ")
    
    ts1 = time.time()
    hr_ts1 = datetime.datetime.fromtimestamp(ts1).strftime('%Y-%m-%d %H:%M:%S')
    print "Processing started at %s" %hr_ts1
    
    wordCount(file_name, min_freq, skill_flag)
    
    ts2 = time.time()
    hr_ts2 = datetime.datetime.fromtimestamp(ts2).strftime('%Y-%m-%d %H:%M:%S')
    print "Processing completed at %s" %hr_ts2
    print "Time elapsed (seconds): %f" %float(ts2-ts1)
