from textTreatment.readFile import Text
from symbolTables.dictSymbolTable import DictSymbolTable
from symbolTables.listSymbolTable import ListSymbolTable
from symbolTables.setSymbolTable import SetSymbolTable
from symbolTables.tupleSymbolTable import TupleSymbolTable
from symbolTables.namedTupleSymbolTable import NamedTupleSymbolTable
from symbolTables.dequeSymbolTable import DequeSymbolTable
from symbolTables.chainMapSymbolTable import ChainMapSymbolTable
from symbolTables.counterSymbolTable import CounterSymbolTable
from symbolTables.defaultDicitSymbolTable import DefaultDictSymbolTable
from symbolTables.orderedDictSymbolTable import OrderedDictSymbolTable
from symbolTables.userDictSymbolTable import UserDictSymbolTable
from symbolTables.userListSymbolTable import UserListSymbolTable
from autoTest import saveAutoTestResults
from pathlib import Path

#path = Path.home() / "programacao" / "python" / "PythonStructuresAnalysis" / "assets" / "leipzig100k.txt" 

#text = Text(path)
#words = text.getWords()
#size = len(words)

# Cria a tabela com os abjetos repectivos 
# tables = {
#     "dict": DictSymbolTable(), 
#     "list": ListSymbolTable(), 
#     "set": SetSymbolTable(),
#     "namedTuple": NamedTupleSymbolTable(),
#     "deque": DequeSymbolTable(),
#     "chainMap": ChainMapSymbolTable(),
#     "counter": CounterSymbolTable(),
#     "defaultDict": DefaultDictSymbolTable(),
#     "orderedDict": OrderedDictSymbolTable(),
#     "userDict": UserDictSymbolTable(),
#     "userList": UserListSymbolTable(),
# }

# # Preenche os objetos com as palavras do arquivo
# for v in tables.values():
#     for word in words:
#         v.put(word)
        
# tables["tuple"] = TupleSymbolTable()
# tables["tuple"].put(words)


#print(tables["dict"])
#print(tables["list"])
#print(tables["set"])
#print(tables["tuple"])
#print(tables["namedTuple"])
#print(tables["deque"])
#print(tables["chainMap"])
#print(tables["counter"])
#print(tables["defaultDict"])
#print(tables["orderedDict"])
#print(tables["userDict"])
#print(tables["userList"])

saveAutoTestResults()