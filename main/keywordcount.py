# Keyword Counter
# Author: Mitul Verma
# Date updated: 25 Sept 2014

from common import stopwords, dictionary

def keywordCount(file_name, min_freq, filter_flag):
    """
    Prints keywords used in a resume text file. The threshold frequency is 
    described by min_freq. The filter_flag enables or disables filtering from
    the skills dictionary.
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

    ## Set up empty list for output. Elements of this list are of the form
    ## [word, frequency].
    output = []

    # Check filter_flag.
    if filter_flag == 'y' or filter_flag == 'Y':
        print "============ Filtering is ON ============"

        ## We split the job into two parts depending on the number of words in
        ## a phrase. Phrases with five or fewer words are handled seperately
        ## from those with six or more words. There are many more dictionary
        ## entries for phrases up to five words and this seperation of labor
        ## means optimal speed and low memory usage.

        # Make five-or-fewer-word phrases using words list.
        five_or_fewer_word_phrases = fiveOrFewerWordPhrases(words)

        # Populate output with five-or-fewer-word phrases by searching through
        # dictionary.
        for i in range(len(five_or_fewer_word_phrases)):
            for phrase in five_or_fewer_word_phrases[i]:
                if phrase in dictionary.five_or_fewer_word_phrases[i]:
                    addWord(phrase, output)


        # Create string of entire resume.
        full_resume = ''
        for word in words:
            full_resume += word
            full_resume += ' '

        # Populate output with six-ore-more-word phrases by searching through
        # full resume.
        for phrase_list in dictionary.six_or_more_word_phrases:            
            for phrase in phrase_list:
                if phrase in full_resume:
                    addWord(phrase, output)

    # If filter_flag is disabled, populate output with one-word-phrases from
    # resume, ignoring stop words and punctuation.
    else:
        print "============ Filtering is OFF ============"
        for word in words:
            word = removePunctuation(word)
            if word not in stopwords.stopwords and word != "":
                addWord(word, output)

    # Order by frequency of occurence or length of keyword. Uncomment the one
    # desired.
    output.sort(key = lambda x: x[1], reverse = True)        # Frequency
    # output.sort(key = lambda x: len(x[0]), reverse = True) # Length

    # count = 0

    # for item in output:
    #     if item[1] >= min_freq:
    #         print item
    #         count +=1

    # print "Total number of keywords: %i" %count

    return output

def fiveOrFewerWordPhrases(words):
    """
    This function constucts one-, two-, three-, four-, and five-word phrases
    from the given list of words. The one-word phrase list is simply the words
    list itself. The function returns a list of these lists of phrases.
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

def removePunctuation(word):
    """
    Removes all non-alphabetical and non-numerical characters from word.
    """
    new_word = ""
    for letter in word:
        if letter.isalpha() or letter.isdigit():
            new_word += letter

    return new_word

def addWord(word, word_list):
    """
    If an instance of word is present in word_list, addWord only increments its
    frequency. Else, it appends word onto word_list with frequency 1.
    """
    for item in word_list:
        if word == item[0]:
            item[1]+=1
            return

    word_list.append([word,1])
    return
