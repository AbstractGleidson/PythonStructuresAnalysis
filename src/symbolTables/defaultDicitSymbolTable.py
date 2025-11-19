from collections import defaultdict

class DefaultDictSymbolTable:
    def __init__(self):
        self.defaultDictWord = defaultdict(None)
        self.count = 0

    def put(self, word: str):
        self.count += 1
        self.defaultDictWord[word] = self.count

    def get(self, word: str) -> str | None:
        return self.defaultDictWord[word] if self.defaultDictWord[word] != "" else None

    def delete(self, word: str):
        if word in self.defaultDictWord:
            del self.defaultDictWord[word]

    def __str__(self):
        return str(dict(self.defaultDictWord))
