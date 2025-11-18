class DictSymbolTable:
    def __init__(self, size: int):
        self.size = size
        self.arrayHash = [{} for _ in range(size)] # Cria uma array preenchido com dicts 
        
    def put(self, word: str):
        dictWord = self.arrayHash[self._hash(word)] # Adiciona um elemento
        dictWord[word] = None
        
    def get(self, word: str):
        dictWord = self.arrayHash[self._hash(word)] # Busca um elemento
        
        if word in dictWord:
            return word
        return None
    
    def delete(self, word: str):
        dictWord = self.arrayHash[self._hash(word)] # Deleta um elemento
        
        if word in dictWord:
            del dictWord[word]
                
    def _hash(self, word): 
        return hash(word) % self.size