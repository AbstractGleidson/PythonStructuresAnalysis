from textTreatment.readFile import Text
from symbolTables.dictSymbolTable import DictSymbolTable
from symbolTables.listSymbolTable import ListSymbolTable
from symbolTables.setSymbolTable import SetSymbolTable
from symbolTables.tupleSymbolTable import TupleSymbolTable
from pathlib import Path

path = Path.home() / "programacao" / "python" / "PythonStructuresAnalysis" / "assets" / "leipzig100k.txt" 

text = Text(path)
words = text.getWords()
size = len(words)

# Cria a tabela com os abjetos repectivos 
tables = {
    "dict": DictSymbolTable(), 
    "list": ListSymbolTable(), 
    "set": SetSymbolTable(),
}

# Preenche os objetos com as palavras do arquivo
for v in tables.values():
    for word in words:
        v.put(word)
        
tables["tuple"] = TupleSymbolTable()

tables["tuple"].put(words)


#print(tables["dict"])
#print(tables["list"])
#print(tables["tuple"])