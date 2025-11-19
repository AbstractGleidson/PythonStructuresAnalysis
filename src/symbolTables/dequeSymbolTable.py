from collections import deque

class DequeSymbolTable:
    def __init__(self):
        self.dequeWords = deque() # Define uma deque para armazenar as palavras
    
    # Adiciona elemento
    def put(self, word: str):
        """
        Adiciona a palavra na deque 
        Args:
            word (str): Palavra que vai ser adicionada 
        """
        self.dequeWords.append(word)
        
    # Recupera elemento
    def get(self, word: str) -> str | None:
        """
        Recupera a palavra da deque 
        Args:
            word (str): Palavra que vai ser pesquisada

        Returns:
            str: Palavra recuperada ou None
        """
        if word in self.dequeWords:
            return word 
        
        return None
    
    # Deleta elemento
    def delete(self, word: str):
        """
        Remove a palavra da deque 
        Args:
            word (str): Palavra que vai ser removida 
        """
        if self.get(word) is not None:
            self.dequeWords.remove(word)
            
    def __str__(self):
        return str(self.dequeWords)