#global
from curses.ascii import isupper, isalpha, isdigit
import sys
from typing import Dict
from operator import itemgetter
from sklearn.neural_network import MLPClassifier

#local
from .globals import CZECH_DIACRITICS_LETTER_MAP, WINDOW_SIZE
from .dataset import Dataset
from .OneHotEncoder import OneHotEncoder


class Test:

    def __init__(self,
                model : MLPClassifier,
                wordCache : Dict,
                oneHotEncoder : OneHotEncoder,
                dataset : Dataset):

        self.model = model
        self.oneHotEncoder = oneHotEncoder
        self.dataset = dataset
        self.wordCache = wordCache

    def findClosestWord(self, diacritisizedWord, nonDiacritisizedWord):
        """
        given a non-diacritisized word, find a word from the wordCache
        dictionary that has the least edit distance to the diacritisized word.
        """
        counts = []
        for word in self.wordCache[nonDiacritisizedWord]:
            editDistance = 0
            for i, j in zip(word, diacritisizedWord):
                if i == j:
                    editDistance += 1
            counts.append((word, editDistance))
        return max(counts, key=itemgetter(1))[0]

    
    def removeDelimiters(self, word):
        newWord = ''
        for i in word:
            if isalpha(i) or isdigit(i):
                newWord += i
        return newWord


    def restoreDelimiters(self, word, wordWithDelimiters):
        if " " in wordWithDelimiters:
            print(word)
        newWord = ""
        index = 0
        for i in range(len(wordWithDelimiters)):
            if not isalpha(wordWithDelimiters[i]) and not isdigit(wordWithDelimiters[i]):
                newWord += wordWithDelimiters[i]
            else:
                newWord += word[index]
                index += 1
        return newWord


    def performPredictionForASingleWord(self, word : str):
        """
        Given a non-diacritisized word, return a word with diacritics
        added after predicting it.
        If the word is already present in the cache, return the closest
        word. Otherwise, we use our letter-trigram language model to predict
        the diacritic marks.
        """

        restoreLetterCasing = lambda x, w: \
            "".join([x[i].upper() if isupper(word[i]) else x[i].lower() for i in range(len(w))])

        addWindowOffset = lambda s : " " * WINDOW_SIZE + s.lower() + " " * WINDOW_SIZE

        wordWithoutDelimiter = self.removeDelimiters(word)

        if wordWithoutDelimiter in self.wordCache:
            return restoreLetterCasing(self.findClosestWord(self.wordCache[wordWithoutDelimiter], wordWithoutDelimiter))
        else:
            newWord = ""
            wordWithOffset = addWindowOffset(wordWithoutDelimiter)
            for j in range(WINDOW_SIZE, len(wordWithOffset) - WINDOW_SIZE):
                if wordWithOffset[j] in CZECH_DIACRITICS_LETTER_MAP:
                    dataWindow = wordWithOffset[j - WINDOW_SIZE : j + WINDOW_SIZE + 1]
                    prediction = self.model.predict(self.oneHotEncoder.getWindowOneHotEncoding(dataWindow).reshape(1, -1))
                    newWord += prediction[0]
                else:
                    newWord += wordWithOffset[j]
            return self.restoreDelimiters(restoreLetterCasing(newWord, wordWithoutDelimiter), wordWithDelimiters=word)



    def performPredictionForASingleLine(self, line : str):
        """
        Given a non-diacritisized line, return a line with diacritics
        added after predicting it.
        """
        return " ".join(self.performPredictionForASingleWord(word) for word in line.split())   


    def performPredictionsFromSTDIN(self):
        """
        read lines from STDIN and predict(add the diacritics).
        """
        for line in sys.stdin:
            lineWithoutDiacritics = line.translate(Dataset.DIACRITICS_TRANSLATE_TABLE)
            lineWithPredictedDiacritics = self.performPredictionForASingleLine(lineWithoutDiacritics)
            print(lineWithPredictedDiacritics)


    def performPredictionsFromTestDataset(self):
        """
        read lines from a file and predict(add the diacritics).
        """
        for line in self.dataset.data:
            lineWithPredictedDiacritics = self.performPredictionForASingleLine(line)
            #print(lineWithPredictedDiacritics)
