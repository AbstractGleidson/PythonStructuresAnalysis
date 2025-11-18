class SetSymbolTable:
    def __init__(self, size: int):
        self.size = size
        self.arrayHash = [set() for _ in range(size)] # Cria um array preenchido com sets
        
    def put(self, word: str):
        self.arrayHash[self._hash(word)].add(word) # Adiciona um elemento
        
    def get(self, word: str): 
        setWords = self.arrayHash[self._hash(word)] # Recupera um elemento
        
        if word in setWords:
            return word
        return None
    
    def delete(self, word: str): # Deleta um elemento 
        setWords = self.arrayHash[self._hash(word)]
                
        if self.get(word) is not None:
            setWords.remove(word) 
        
    def _hash(self, word: str):
        return hash(word) % self.size