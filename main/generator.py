# the main wordcloud generator

import time
import matplotlib.pyplot as plt
from wordcloud2 import WordCloud

def makeWordCloud(file_name, min_freq, filter_flag):

    wordcloud = WordCloud().generate(file_name, min_freq, filter_flag)
    # Open a plot of the generated image.
    plt.imshow(wordcloud)
    plt.axis("off")
    pic_name = file_name[:-4] + str(min_freq) + filter_flag + '.png'
    plt.savefig(pic_name, bbox_inches='tight')

if __name__ == "__main__":

    file_name = raw_input("Path to text file: ")
    min_freq = int(raw_input("Minimum frequency of keywords: "))
    filter_flag = raw_input("Filter keywords from skills dictionary? (y/n): ")
    
    before = time.time()
    makeWordCloud(file_name, min_freq, filter_flag)
    after = time.time()

    print "Processing time (seconds): %f" %float(after - before)
