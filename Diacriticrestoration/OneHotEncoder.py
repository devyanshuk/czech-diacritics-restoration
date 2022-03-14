#global
import numpy as np

class OneHotEncoder:

    @staticmethod
    def getOneHotEncodingForACharacter(x):
        """
        returns a one-hot encoding for a char
        """
        oneHotEncoding = [0] * ord(x) + [1] + [0] * (127 - ord(x))

        if len(oneHotEncoding) != 128:
            raise Exception("wrong one-hot encoding.")

        return oneHotEncoding


    def getWindowOneHotEncoding(self, window : str):
        """
        Given a string(window), return a list of all its one-hot encoded
        characters.

        :params window : word to one-hot encode
        """
        oneHotEncoding = []
        for char in window:
            oneHotEncoding += self.getOneHotEncodingForACharacter(char)
        return np.array(oneHotEncoding)