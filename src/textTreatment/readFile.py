class Text:
    def __init__(self, path):
        with open(path,  "r", encoding="UTF-8") as file:
            self.text  = file.read() # Ler o arquivo texto e adcionar a string em text
            
    def getWords(self):
        return self.text.split()