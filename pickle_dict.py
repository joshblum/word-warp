"""
    Parses flat text file of english words and writes them into a pickle dictionary
"""
import pickle
import os

from constants import WORDS_FILE, DICT_FILE


def main():

    word_dict = dict.fromkeys([3, 4, 5, 6], set())
    print "Starting..."
    print "Reading", WORDS_FILE
    valid_sizes = set(range(3, 7))
    with open(WORDS_FILE) as f:
        for line in f:
            word = line.strip(os.linesep)
            size = len(word)
            if size in valid_sizes:
                print word_dict[size]
                word_dict[size].add(word)
    print "Writing pickle", DICT_FILE
    with open(DICT_FILE, 'wb') as pickle_dict:
        pickle.dump(word_dict, pickle_dict)
    print "Done."

if __name__ == "__main__":
    main()
