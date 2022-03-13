#global
import os
import ssl
import urllib.request

#local
from .globals import makeDiacriticsToNoDiacriticsMap

class Dataset:

    """
    Loads the data from trainPath and removes the diacritic symbols for further
    processing.
    """

    DIACRITICS_TRANSLATE_TABLE = str.maketrans(makeDiacriticsToNoDiacriticsMap())

    def __init__(self,
                url=None,
                path=None):
        
        if url is not None and not os.path.exists(path):
            print(f"Downloading dataset {path}...")
            if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):
                ssl._create_default_https_context = ssl._create_unverified_context
            urllib.request.urlretrieve(f"{url}/{path}", filename=path)

        with open(path, "r") as inputFile:
            target = inputFile.read()
            self.target = target.splitlines()
        self.data = target.translate(self.DIACRITICS_TRANSLATE_TABLE).splitlines()