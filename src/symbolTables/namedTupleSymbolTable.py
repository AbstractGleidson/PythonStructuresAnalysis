from collections import namedtuple

class NamedTupleSymbolTable:
    def __init__(self):
        self.wordTuple = namedtuple("Words", ["word", "count"]) # Definindo uma namedTuple 
        self.namedTupleWords = [] # Definindo uma lista para armazenar as namedTuples
        self.count = 0 # Quantidade de palavras
        
    # Adiciona elemento
    def put(self, word: str):
        """
        Cria um namedTuple para a palavra e adiciona na lista de de namedTuples 
        Args:
            word (str): Palavra que vai ser adiciona na lista de namedTuples
        """
        
        self.count += 1 # Incrementa quantidade de palavras 
        self.namedTupleWords.append(self.wordTuple(word, self.count)) # Adiciona um novo namedTuple na lista 
    
    # Recupera elemento
    def get(self, word: str):
        """
        Recupera uma namedTuple de acordo com a palavra passada como parametro
        Args:
            word (str): Palavra que vai ser recuperada
            
        Returns:
            namedtuple | None: Retorna uma namedtuple com a palavra  caso esteja na lista, caso contrario retorna None
        """
        for namedTuple in self.namedTupleWords:
            if namedTuple.word == word: 
                return namedTuple
            
        return None
    
    # Deleta elemento
    def delete(self, word: str):
        """
        Remove o namedTuple da palavra da lista de namedTuple se ela estiver na lista
        Args:
            word (str): Palavra que vai ser removida 
        """
        for index, namedTuple in enumerate(self.namedTupleWords): # Enumara para conseguir achar o index 
            if namedTuple.word == word:
                self.namedTupleWords.pop(index)
    
    def __str__(self):
        return str(self.namedTupleWords)