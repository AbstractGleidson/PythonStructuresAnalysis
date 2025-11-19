from collections import ChainMap

class ChainMapSymbolTable:
    def __init__(self):
        self.chainWord = ChainMap({})  # mapa principal no topo
        self.count = 0
    
    def put(self, word: str):
        self.count += 1
        self.chainWord[word] = self.count

    def get(self, word: str) -> str | None:
        return self.chainWord.get(word, None)

    def delete(self, word: str):
        if word in self.chainWord:
            del self.chainWord[word]

    def __str__(self):
        return str(self.chainWord)
