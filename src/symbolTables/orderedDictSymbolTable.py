from collections import OrderedDict

class OrderedDictSymbolTable:
    def __init__(self):
        self.odict = OrderedDict()
        self.count = 0

    def put(self, word: str):
        self.count += 1
        self.odict[word] = self.count

    def get(self, word: str) -> str | None:
        return self.odict.get(word, None)

    def delete(self, word: str):
        if word in self.odict:
            del self.odict[word]

    def __str__(self):
        return str(self.odict)