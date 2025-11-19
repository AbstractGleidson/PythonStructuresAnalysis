import json
import time
from pathlib import Path

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


# Cria um dicionario com as instancias de cada tabela de simbolos 
def create_tables():
    return {
        "dict": DictSymbolTable(),
        "list": ListSymbolTable(),
        "set": SetSymbolTable(),
        "tuple": TupleSymbolTable(),        
        "namedTuple": NamedTupleSymbolTable(),
        "deque": DequeSymbolTable(),
        "chainMap": ChainMapSymbolTable(),
        "counter": CounterSymbolTable(),
        "defaultDict": DefaultDictSymbolTable(),
        "orderedDict": OrderedDictSymbolTable(),
        "userDict": UserDictSymbolTable(),
        "userList": UserListSymbolTable(),
    }

# Realiza os testes de forma automatica 
def autoTestInsert(words: list[str], steps=10):
    results = {}

    for name in create_tables().keys():

        total_time = 0.0 

        for _ in range(steps): # Roda steps vezes para cada estrutura 
            table = create_tables()[name] # Pega uma instancia da estrutura atual

            start = time.perf_counter() # Calcula o tempo de inicio

            if name == "tuple": # Caso especial de insercao para tuplas
                table.put(words)
            else:
                for w in words:
                    table.put(w)

            end = time.perf_counter() # Calcula o tempo final

            total_time += (end - start)

        results[name] = total_time / steps # Tira a media 

    return results

# Realiza os testes de forma automatica 
def autoTestGet(words: list[str], getWords: list[str], steps=10):
    structures = create_tables()
    results = {}

    # Preenche as estruturas
    for name in structures.keys():
        if name == "tuple": # Caso especial de insercao para tuplas
            structures[name].put(words)
        else:
            for w in words:
                structures[name].put(w)
                
    # Pesquisa as palavras
    for name in structures.keys():
        total_time = 0.0
        
        for _ in range(steps):
            
            start = time.perf_counter() # Inicio do tempo de execucao
            
            # Realiza a busca por cada palavra            
            for word in getWords:
                structures[name].get(word)

            end = time.perf_counter() # Fim do tempo de execucao

            total_time += (end - start)
        
        results[name] = total_time / steps
    
    return results

# Realiza os testes de forma automatica 
def autoTestDelete(words: list[str], getWords: list[str], steps=10):
    structures = create_tables()
    results = {}

    # Preenche as estruturas
    for name in structures.keys():
        if name == "tuple": # Caso especial de insercao para tuplas
            structures[name].put(words)
        else:
            for w in words:
                structures[name].put(w)
                
    # Deleta palavras
    for name in structures.keys():
        total_time = 0.0
        
        for _ in range(steps):
            
            start = time.perf_counter() # Inicio do tempo de execucao
            
            # Realiza a busca por cada palavra            
            for word in getWords:
                structures[name].delete(word)

            end = time.perf_counter() # Fim do tempo de execucao

            total_time += (end - start)
        
        results[name] = total_time / steps
    
    return results


# Salva resultado em um json
def saveAutoTestResults(path: str, results: dict):
    with open(path, "w", encoding="utf-8") as file:
        json.dump(results, file, indent=4)

    print("\nJSON salvo em:", path)