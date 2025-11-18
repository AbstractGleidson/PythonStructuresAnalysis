class DictSymbolTable:
    def __init__(self):
        self.dictWords = dict() # Dict para armazenar os elementos
        self.count = 0 # Quantidade elementos na estrutura
        
    # Adiciona elemento 
    def put(self, word: str):
        """
        Adiciona uma string no dict com a palavra sendo a key e a quantidade o valor
        Args:
            word (str): Palavra que vai ser inserida
        """
         
        self.count += 1 # Incrementa a quantidade de elementos 
        self.dictWords[word] = self.count # Adiciona a palavra como key e a quantidade como valor
        
    # Recupera elemento
    def get(self, word: str) -> str | None: 
        """
        Pesquisa uma palavra no dict
        Args:
            word (str): palavra recuperada

        Returns:
              str | None: a palavra que esta sendo procurada ou None
        """
        
        if word in self.dictWords:
            return word
        return None
    
    # Deleta elemento 
    def delete(self, word: str): 
        """
        Deleta uma palavra do dict
        Args:
            word (str): Palavra que vai ser deletada
        """
    
        if self.get(word) is not None: 
            self.dictWords.pop(word, None)
    
    def __str__(self):
        return str(self.dictWords)