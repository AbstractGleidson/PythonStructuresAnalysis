import re

class Text:
    def __init__(self, path):
        with open(path,  "r", encoding="UTF-8") as file:
            self.text  = file.read() # Ler o arquivo texto e adcionar a string em text
            
    def getWords(self):
        return re.findall(r"[A-Aa-z]+", self.text) # O regex considera apenas letras 