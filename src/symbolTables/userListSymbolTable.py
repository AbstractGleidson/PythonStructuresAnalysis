from collections import UserList

class UserListSymbolTable(UserList):
    def __init__(self):
        super().__init__()

    def put(self, word: str):
        self.data.append(word)

    def get(self, word: str) -> str | None:
        if word in self.data:
            return word
        return None

    def delete(self, word: str):
        if word in self.data:
            self.data.remove(word)

    def __str__(self):
        return str(self.data)
