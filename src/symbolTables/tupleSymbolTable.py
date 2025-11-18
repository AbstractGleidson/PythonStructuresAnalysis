class TupleSymbolTable:
    def __init__(self):
        self.tupleWords = tuple() # Cria uma tupla do python
                
    # Adiciona uma lista de elementos
    def put(self, words: list[str]):
        """
        Adiciona uma lista de elementos passados como parametro na tupla
        Args:
            word (list[str]): Elementos que devem ser inseridos na tupla
        """
        self.tupleWords = self.tupleWords + tuple(words)
    
    # Recupera elemento
    def get(self, word: str) -> str | None:
        """
        Recupera a palavra passada como parametro, caso ela esteja na tupla
        Args:
            word (str): Palavra que vai ser procurada

        Returns:
               str | None: Retorna a palavra caso esteja na tupla, caso contrario retorna None
        """
        
        if word in self.tupleWords:
            return word
        return None 
    
    # Deleta elemento
    def delete(self, word: str):
        """
        Remove a palavra passada como parametro da tupla se ela estiver na tupla
        Args:
            word (str): Palavra para ser removida da tupla
        """
        
        if self.get(word) is not None:
            self.tupleWords = tuple(w for w in self.tupleWords if w is not word) # Cria uma nova tupla sem essa palavra
            
    def __str__(self):
        return str(self.tupleWords)