import json
from pathlib import Path

def readDataBase(path):
    data = {}
    
    with open(path, "r", encoding="UTF-8") as file:
        data = json.load(file)
        
    return dict(data)    