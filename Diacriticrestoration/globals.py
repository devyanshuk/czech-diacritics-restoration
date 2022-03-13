CZECH_DIACRITICS_LETTER_MAP = {
    'a' : 'á',
    'c' : 'č',
    'd' : 'ď',
    'e' : ['é', 'ě'],
    'i' : 'í',
    'n' : 'ň',
    'o' : 'ó',
    'r' : 'ř',
    's' : 'š',
    't' : 'ť',
    'u' : ['ú', 'ů'],
    'y' : 'ý',
    'z' : 'ž'
}

WINDOW_SIZE = 3

def makeDiacriticsToNoDiacriticsMap():
    """
    maps non-diacritisized characters with its diacritisized variant, for both the lower
    and the upper variants, which then will be used to remove the diacritics in the
    train data to train the model.
    """

    map = {}

    for key, value in CZECH_DIACRITICS_LETTER_MAP.items():
        if isinstance(value, list):
            for i in value:
                map[i] = key
                map[i.upper()] = key.upper()
        else:
            map[value] = key
            map[value.upper()] = key.upper()
    return map


