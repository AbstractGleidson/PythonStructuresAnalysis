class ListSymbolTable:
    def __init__(self, size: int):
        self.size = size
        self.arrayHash = [[] for _ in range(size)] # Cria uma lista do python
                
    def put(self, word: str):
        self.arrayHash[self._hash(word)].append(word) # Adiciona a palavra em uma posicao da lista #type: ignore
        
    def get(self, word: str):
        for wordList in self.arrayHash[self._hash(word)]: # Recupera a palavra
            if word == wordList:
                return wordList # caso encontre a palavra
    
        return None # Caso nao encontre a palavra 
    
    def delete(self, word: str):
        if self.get(word) != None:
            self.arrayHash[self._hash(word)].remove(word) # Deleta a palavra
        
    def _hash(self, word: str):
        return hash(word) % self.size # Funcao hash