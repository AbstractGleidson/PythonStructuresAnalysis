class ListSymbolTable:
    def __init__(self):
        self.listWords = list() # Cria uma lista do python
                
    # Adiciona elemento
    def put(self, word: str):
        """
        Adiciona o elemento passado como parametro na lista
        Args:
            word (str): Elemento que vai ser inserido na lista
        """
        self.listWords.append(word)
    
    # Recupera elemento
    def get(self, word: str) -> str | None:
        """
        Recupera a palavra passada como parametro, caso ela esteja na lista
        Args:
            word (str): Palavra que vai ser procurada

        Returns:
               str | None: Retorna a palavra caso esteja na lista, caso contrario retorna None
        """
        
        if word in self.listWords:
            return word
        return None 
    
    # Deleta elemento
    def delete(self, word: str):
        """
        Remove a palavra passada como parametro da lista se ela estiver na lista
        Args:
            word (str): Palavra para ser removida da lista
        """
        
        if self.get(word) is not None:
            self.listWords.remove(word)
            
    def __str__(self):
        return str(self.listWords)