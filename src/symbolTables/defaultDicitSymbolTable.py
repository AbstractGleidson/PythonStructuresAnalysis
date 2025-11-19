from collections import defaultdict

class DefaultDictSymbolTable:
    def __init__(self):
        # defaultdict precisa de uma função. Usamos lambda: None para retornar None.
        self.defaultDictWord = defaultdict(lambda: None)

    def put(self, word: str):
        self.defaultDictWord[word] = word # type: ignore

    def get(self, word: str) -> str | None:
        return self.defaultDictWord.get(word, None)

    def delete(self, word: str):
        if word in self.defaultDictWord:
            del self.defaultDictWord[word]

    def __str__(self):
        # converter para dict remove o comportamento de defaultdict na impressão
        return str(dict(self.defaultDictWord))
