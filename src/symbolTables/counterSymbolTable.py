from collections import Counter

class CounterSymbolTable:
    def __init__(self):
        self.counterWord = Counter()

    def put(self, word: str):
        self.counterWord[word] += 1

    def get(self, word: str) -> str | None:
        if self.counterWord[word] > 0:
            return word
        return None

    def delete(self, word: str):
        if word in self.counterWord:
            del self.counterWord[word]

    def __str__(self):
        return str(self.counterWord)
