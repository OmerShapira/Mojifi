import json
from collections import defaultdict


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

    def clean(self, s):
        return unicode(s).lower()

    def __setitem__(self, key, value):
        if not self.is_locked:
            islist = lambda x: isinstance(x, list)
            keys_as_list = [self.clean(k) for k in key] if islist(key) else [self.clean(key)]
            # Add a set unless it's there
            superclass = super(SymbolDictionary, self)
            value_as_list = value if islist(value) else [value]
            for k in keys_as_list:
                #FIXME: Check if values as lists are still neccessary
                if superclass.__contains__(k):
                    # Non-functional
                    superclass.__getitem__(k).extend(value_as_list)
                else:
                    superclass.__setitem__(k, value_as_list)

    def __getitem__(self, key):
        return super(SymbolDictionary, self).__getitem__(self.clean(key))

    def __missing__(self, key):
        #TODO: Implement this sucker
        pass



def test(d):
    pass


def main():
    d = SymbolDictionary("/Users/Omer/dev/Mojifi/emoji-clean.json", None)
    print d["swim"]
    # test(d)


if __name__ == '__main__':
    main()
