from constants import *

from itertools import permutations
import random
import pickle

#mport pdb; pdb.set_trace()
           
class WordWarp():

    def __init__(self):
        
        self.cmds = {
            'warp' : 'warp!',
            'exit' : '_exit',
            'words' : 'words_left',
            'start' : 'start_game',
            'help' : 'help!',
            'ans' : 'ANSWERS',
        }

        self.funcs = {
            self.cmds['warp'] : self.warp,
            self.cmds['words'] : self.words_left,
            self.cmds['start'] : self.new_game,
            self.cmds['exit'] : self.kill_game,
            self.cmds['ans'] : self.print_ans,
            self.cmds['help'] : self.help_menu,
        }

        self.help = [
            'To check the number of words left enter "%s".' % self.cmds['words'],
            'To warp type "%s".' % self.cmds['warp'],
            'Exit by pressing typing "%s".' % self.cmds['exit'],
            'Start a new game by entering "%s".' % self.cmds['start'],
            'To see these options again type "%s".' % self.cmds['help'],
        ]

        self.end = "Level complete!\ntype '%s' for a new level!" % self.cmds['start']

        self.dict_words = self.get_dict_words()

    def get_dict_words(self):
        return pickle.load(open(DICT_FILE))

    def help_menu(self):
        for line in self.help:
            print line

    def new_game(self):
        self.help_menu()
        self.get_words()
        self.words_left()
        self.warp()
        
    def get_words(self):
        """
            Selects a random six letter word and generates 3, 4, 5 word length permutations. Returns scrambled word.
        """
        self.answer = random.choice(self.dict_words[6].keys())
        self.answer_perms = [''.join(perm) for perm in permutations(self.answer, 6)]
        
        self.words = {}
        for i in range(6, 2, -1):
            perm = permutations(self.answer, i)
            self.words[i] = self.real_words(perm, i)

        self.list_lengths = {}
        for key, value in self.words.items():
            self.list_lengths[key] = len(value)

    def real_words(self, word_perms, word_length):
        """
            Given a search list of permutations, generates and returns a dictionary of real words from this list.
        """
        real_dict = {}
        for perm in word_perms:
            perm = ''.join(perm)
            if perm in self.dict_words[word_length]:
                real_dict[perm] = ''
        return real_dict
    
    def check_word(self, word):
        word_length = len(word)
        
        if word_length in range(3, 7) and word in self.words[word_length]:
            self.list_lengths[word_length] -= 1
            self.check_end_game()

    def check_end_game(self):
        if not self.list_lengths[6]:
            print self.end
            
    def warp(self):
        print random.choice(self.answer_perms)
        
    def words_left(self):
        for index, length in enumerate(self.list_lengths):
            print 'The number of %s letter words is %s.' % (length, self.list_lengths[index +3])

    def kill_game(self):
        print "Goodbye!"
        self.game = False

    def print_ans(self):
        word_map = {
            3 : 'Three',
            4 : 'Four',
            5 : 'Five',
            6 : 'Six',
        }
        for key, value in word_map.items():
            print "%s letter words: %s" % (value, self.words[key].keys())
            
    def play(self):
        self.game = True

        self.new_game()

        while self.game:
            word = raw_input('> ')
            func = self.funcs.get(word)
            if func:
                func()
            else:
                self.check_word(word)
            
def main():
    game = WordWarp()
    game.play()
    
if __name__ == "__main__":
    main()              