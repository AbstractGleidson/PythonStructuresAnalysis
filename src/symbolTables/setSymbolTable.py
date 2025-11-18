class SetSymbolTable:
    def __init__(self):
        self.setWords = set() # Cria uma set() do python
                
    # Adiciona elemento
    def put(self, word: str):
        """
        Adiciona o elemento passado como parametro no set
        Args:
            word (str): Elemento que vai ser inserido no set
        """
        self.setWords.add(word)
    
    # Recupera elemento
    def get(self, word: str) -> str | None:
        """
        Recupera a palavra passada como parametro, caso ela esteja no set
        Args:
            word (str): Palavra que vai ser procurada

        Returns:
               str | None: Retorna a palavra caso esteja no set, caso contrario retorna None
        """
        
        if word in self.setWords:
            return word
        return None 
    
    # Deleta elemento
    def delete(self, word: str):
        """
        Remove a palavra passada como parametro do set se ela estiver no set
        Args:
            word (str): Palavra para ser removida do set
        """
        if self.get(word) is not None:
            self.setWords.remove(word)