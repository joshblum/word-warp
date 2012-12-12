"""
    Parses flat text file of english words and writes them into a pickle dictionary
"""
from constants import *

import pickle

def main():
    
    word_dict = {
        3 : {},
        4 : {},
        5 : {},
        6 : {},
    }
    print "Starting..."
    print "Reading", WORDS_FILE
    with open(WORDS_FILE) as f:
        for line in f:
            word = line.strip('\r\n')
            size = len(word)
            if size in range(3,7):
                dic = word_dict[size]
                dic[word] = word
    print "Writing pickle", DICT_FILE
    with  open(DICT_FILE, 'wb') as pickle_dict:
        pickle.dump(word_dict, pickle_dict)
    print "Done."

if __name__ == "__main__":
    main()