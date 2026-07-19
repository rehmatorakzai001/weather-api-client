import json

def read():
    with open("history.json", 'r') as file:
        return json.load(file)

def write(record):
    with open("history.json", 'w') as file:
        json.dump(record, file)
