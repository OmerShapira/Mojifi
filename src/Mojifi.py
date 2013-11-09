import json
from collections import defaultdict

from nltk.tokenize.punkt import PunktWordTokenizer


def clean(s):
        return unicode(s).lower()


class SymbolDictionary(defaultdict):
    """Wrapper class containing translator functions"""
    def __init__(self, filename, encoding):
        super(SymbolDictionary, self).__init__()
        self.filename = filename
        self.encoding = encoding
        self.is_locked = False
        with open(self.filename) as f:
            table_key_to_vals = json.load(f, encoding=self.encoding)
            for key, value in table_key_to_vals.iteritems():
                # Reverse the keys to vals
                self.__setitem__(value, key)

        self.is_locked = True

    def __setitem__(self, key, value):
        if not self.is_locked:
            islist = lambda x: isinstance(x, list)
            key_list = [clean(k) for k in key] if islist(key) else [clean(key)]
            # Add a set unless it's there
            superclass = super(SymbolDictionary, self)
            value_as_list = value if islist(value) else [value]
            for k in key_list:
                #FIXME: Check if values as lists are still neccessary
                if superclass.__contains__(k):
                    # Non-functional
                    superclass.__getitem__(k).extend(value_as_list)
                else:
                    superclass.__setitem__(k, value_as_list)

    def __getitem__(self, key):
        return super(SymbolDictionary, self).__getitem__(clean(key))

    def __missing__(self, key):
        #TODO: Implement this sucker
        pass


class Translator:
    """docstring for Translator"""
    def __init__(self, *dictionaries):
        self.tokenizer = PunktWordTokenizer()
        self.dictionaries = dictionaries

    def translate(self, sentence):
        tokens = self.tokenizer.tokenize(sentence)

        def select_value(l):
            '''Should select the corect value'''
            #TODO: Implement
            if isinstance(l, list):
                return l[0]
            else:
                return l

        def tr(word):
            for d in self.dictionaries:
                found = d[word]
                if found is not None:
                    return found
            else:
                return word

        return [select_value(tr(w)) for w in tokens]
        # return ' '.join([tr(w) for w in tokens])


#############################################################################

def test(d):
    pass


def main():
    d = SymbolDictionary("/Users/Omer/dev/Mojifi/emoji-mdown.json", None)
    t = Translator(d)
    print t.translate("The quick brown fox jumps over the lazy dog")


if __name__ == '__main__':
    main()
