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
from autoTest import saveAutoTestResults, autoTestGet, autoTestInsert, autoTestDelete
from textTreatment.readJson import readDataBase
from generatesGraphs.generatesBarChart import barChart
from pathlib import Path

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


# Teste de insercao
# pathText = Path.home() / "programacao" / "python" / "PythonStructuresAnalysis" / "assets" / "leipzig100k.txt"
# words = Text(pathText).getWords() # Ler palavras do arquivo 

# path = Path.home() / "programacao" / "python" / "PythonStructuresAnalysis" / "src" / "database" / "insertionTime.json" 
# saveAutoTestResults(str(path), autoTestInsert(words))

# Teste de busca
# pathText = Path.home() / "programacao" / "python" / "PythonStructuresAnalysis" / "assets" / "leipzig100k.txt"
# words = Text(pathText).getWords() # Ler palavras do arquivo 

# path = Path.home() / "programacao" / "python" / "PythonStructuresAnalysis" / "src" / "database" / "getTime.json" 
# saveAutoTestResults(str(path), autoTestGet(words, ["Lisbon", "NASA", "Kyunghee", "Konkuk", "Sogang", "momentarily", "rubella", "vaccinations", "government", "Authorities"]))

# Teste de delete
# pathText = Path.home() / "programacao" / "python" / "PythonStructuresAnalysis" / "assets" / "leipzig100k.txt"
# words = Text(pathText).getWords() # Ler palavras do arquivo 

# path = Path.home() / "programacao" / "python" / "PythonStructuresAnalysis" / "src" / "database" / "deleteTime.json" 
# saveAutoTestResults(str(path), autoTestDelete(words, ["Lisbon", "NASA", "Kyunghee", "Konkuk", "Sogang", "momentarily", "rubella", "vaccinations", "government", "Authorities"]))

# datas = dict(readDataBase( path = Path.home() / "programacao" / "python" / "PythonStructuresAnalysis" / "src" / "database" / "insertionTime.json"))
# structuresName = []
# times = []

# for name, time in datas.items():
#     structuresName.append(name)
#     times.append(time * 1000) # Converte pra milisegundos
        
# barChart(structuresName, times)