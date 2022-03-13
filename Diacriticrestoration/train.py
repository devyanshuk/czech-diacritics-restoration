#global
import pickle
import lzma
import numpy as np
from curses.ascii import isalpha, isdigit
from sklearn.neural_network import MLPClassifier

#local
from .dataset import Dataset
from .globals import CZECH_DIACRITICS_LETTER_MAP, WINDOW_SIZE
from .OneHotEncoder import OneHotEncoder


class Train:

    def __init__(self,
                oneHotEncoder : OneHotEncoder, 
                dataset : Dataset,
                modelPath : str):

        self.modelPath = modelPath
        self.dataset = dataset
        self.model = None
        self.oneHotEncoder = oneHotEncoder
        self.wordCache = {}


    def storeWordInCache(self, nonDiacritisizedWord, diacritisizedWord):
        """
        Add the non-diacritisized word as a key of the wordCache dictionary,
        with diacritisizedWord being it's corresponging value.
        """
        if nonDiacritisizedWord == "":
            return
        if nonDiacritisizedWord in self.wordCache:
            self.wordCache[nonDiacritisizedWord].append(diacritisizedWord)
        else:
            self.wordCache[nonDiacritisizedWord] = [diacritisizedWord]


    def storeWordsInCache(self, dataLine, targetLine):
        """
        Given a non-diacritisized line and it's corresponding diacritisized line,
        store a non-diacritisized : diacritisized map in wordCache
        """
        data = dataLine.split()
        target = targetLine.split()
        for d, t in zip(data, target):
            noDelimiterData, noDelimiterTarget = "", ""
            for i in range(len(d)):
                if (isalpha(i) or isdigit(i)):
                    noDelimiterData += d[i]
                    noDelimiterTarget += t[i]
            self.storeWordInCache(noDelimiterData.strip(), noDelimiterTarget.strip())


    def trainModel(self):
        """
        Trains a letter-trigram language model using the specified window size,
        transforming the window to one-hot encoding and fitting the train and test
        data.
        """
        model = MLPClassifier()
        oneHotEncodedData, oneHotEncodedTarget = [], []

        addWindowOffset = lambda s : " " * WINDOW_SIZE + s.lower() + " " * WINDOW_SIZE

        for i in range(len(self.dataset.data)):
            data, target = addWindowOffset(self.dataset.data[i]), addWindowOffset(self.dataset.target[i])
            self.storeWordsInCache(data, target)
            for j in range(WINDOW_SIZE, len(self.dataset.data) - WINDOW_SIZE):
                if data[j] in CZECH_DIACRITICS_LETTER_MAP:
                    dataWindow = data[j - WINDOW_SIZE : j + WINDOW_SIZE + 1]
                    targetChar = target[j]
                    oneHotEncodedData.append(self.oneHotEncoder.getWindowOneHotEncoding(dataWindow))
                    oneHotEncodedTarget.append(targetChar)
        oneHotEncodedData = np.array(oneHotEncodedData)
        self.oneHotEncodedTarget = np.array(oneHotEncodedTarget)
        model.fit(oneHotEncodedData, oneHotEncodedTarget)

    
    def saveModel(self):
        """
        Saves the model to the specified file.
        """
        with lzma.open(self.modelPath, "wb") as modelFile:
            pickle.dump(self.model, modelFile)

                
    def loadModel(self):
        """"
        loads the MLPClassifier model from the specified file
        and stores it to model field.
        """
        with lzma.open(self.modelPath, "rb") as modelFile:
            self.model, _ = pickle.load(modelFile)