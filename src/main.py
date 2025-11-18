from textTreatment.readFile import Text
from symbolTables.dictSymbolTable import DictSymbolTable
from symbolTables.listSymbolTable import ListSymbolTable
from symbolTables.setSymbolTable import SetSymbolTable
from pathlib import Path

path = Path.home() / "programacao" / "python" / "PythonStructuresAnalysis" / "assets" / "leipzig100k.txt" 

text = Text(path)
words = text.getWords()
size = len(words)

# Cria a tabela com os abjetos repectivos 
tables = {
    "dict": DictSymbolTable(size), 
    "list": ListSymbolTable(size), 
    "set": SetSymbolTable(size)
}

# Preenche os objetos com as palavras do arquivo
for v in tables.values():
    for word in words:
        v.put(word)