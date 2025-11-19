from collections import UserDict

class UserDictSymbolTable(UserDict):
    def __init__(self):
        super().__init__()
        self.count = 0

    def put(self, word: str):
        self.count += 1
        self.data[word] = self.count

    def get(self, word: str) -> str | None:
        return self.data.get(word, None)

    def delete(self, word: str):
        if word in self.data:
            del self.data[word]

    def __str__(self):
        return str(self.data)
