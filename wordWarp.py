import itertools
import random
import ENDict
           
class wordWarp():
    def __init__(self):
         self.letterNum = {'a':0 , 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8, 'j':9,
                     'k':10,'l':11, 'm':12, 'n':13, 'o':14, 'p':15, 'q':16, 'r':17, 's':18,
                     't':19, 'u':20, 'v':21, 'w':22, 'x':23, 'y':24, 'z':25}
    def newGame(self):
        self.helpMenu()
        self.string = random.choice(ENDict.dic6[random.choice(range(26))])
        self.perm6 = list(itertools.permutations(self.string, 6))
        self.words6 = list(set(self.realWords(self.perm6)))
        self.perm5 = list(itertools.permutations(self.string, 5))
        self.words5 = list(set(self.realWords(self.perm5)))
        self.perm4 = list(itertools.permutations(self.string, 4))
        self.words4 = list(set(self.realWords(self.perm4)))
        self.perm3 = list(itertools.permutations(self.string, 3))
        self.words3 = list(set(self.realWords(self.perm3)))
        self.listLengths = [len(self.words3), len(self.words4), len(self.words5), len(self.words6)]
        self.wordsLeft()
        print self.warp()
        
    def helpMenu(self):
        print 'To check the number of words left enter "wordsLeft".'
        print 'To warp type "warp!".'
        print 'Exit by pressing typing "EXIT", start a new game by entering "startGame()".'
        print 'To see these options again type "help!".'
        
    def realWords(self,searchList):
        realWords = []
        self.dicReals = {3:ENDict.dic3, 4:ENDict.dic4, 5:ENDict.dic5, 6:ENDict.dic6}
        wordLen = len(searchList[0])
        def stringed(z):
            stringZ= ''
            for letter in z:
                stringZ += letter
            return stringZ
        for x in searchList:
            index = self.letterNum[x[0]]
            searching = self.dicReals[wordLen][index]
            for y in searching:
                if y == stringed(x):
                    realWords.append(y)
        return realWords
    
    def realWord(self, word):
        self.dicWords = {3:self.words3, 4:self.words4, 5:self.words5, 6:self.words6}
        wordLen = len(word)
        if wordLen < 3 or wordLen > 6:
            pass
        else:
            searching = self.dicWords[wordLen]
            popIn = 0
            for y in searching:
                if y == word: 
                    self.dicWords[wordLen].pop(popIn)
                    self.listLengths[wordLen-3] -=1
                    if self.listLengths[3] == 0:
                        print "Level complete!\ntype 'startGame()' for a new level!"

                else:
                    popIn += 1
            
    def warp(self):
            return str(random.choice(self.perm6))
        
    def wordsLeft(self):
        index = 3
        for x in self.listLengths:
            print 'The number of ' + str(index) + ' letter words is ' + str(x) +'.'
            index +=1
            
    def playGame(self):
        game = True
        self.newGame()
        while game == True:
            word = raw_input('>')
            print '>',
            if word == "warp!":
                print self.warp()
            elif word == "wordsLeft":
                self.wordsLeft()
            elif word == "startGame()":
                return startGame()
            elif word == "EXIT":
                print "Goodbye!"
                game = False
            elif word == "ANSWERS":
                print "Three letter words: " + str(self.words3)
                print "Four letter words: " + str(self.words4)
                print "Five letter words: " + str(self.words5)
                print "Six letter words: " + str(self.words6)
            elif word == "help!":
                self.helpMenu()
            else:
                self.realWord(word)
            
def startGame():
    game = wordWarp()
    game.playGame()
    

startGame()
            
            
        
                     
    
            
    
    
        

