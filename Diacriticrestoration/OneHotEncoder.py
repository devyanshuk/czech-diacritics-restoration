#global
import numpy as np

class OneHotEncoder:

    def __init__(self):
        self.oneHotEncoderCache = self.getOneHotEncoderCache()

    @staticmethod
    def getOneHotEncoderCache():
        """
        returns a dictionary with keys as all the 128 ascii characters
        that are mapped to its corresponding one-hot encoding.
        """
        oneHotEncoding = lambda x : [0] * x + [1] + [0] * (127 - x)

        cache = {}
        for i in range(128):
            cache[chr(i)] = oneHotEncoding(i)
            if len(oneHotEncoding(i)) != 128:
                raise Exception("wrong one-hot encoding.")
        return cache

    def getWindowOneHotEncoding(self, window : str):
        """
        Given a string(window), return a list of all its one-hot encoded
        characters.

        :params window : word to one-hot encode
        """
        oneHotEncoding = []
        for char in window:
            oneHotEncoding += self.oneHotEncoderCache[char]
        return np.array(oneHotEncoding)