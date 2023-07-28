import json


DATA_FILE ='contacts.json'

""" read the JSON document from file"""
def load(DATA_FILE):
    with open(DATA_FILE,'r') as json_file:
       data = json.load(json_file)
       return data
    

"""converts a Python object into a JSON and writes it to a file"""
def save(contacts):
    with open(DATA_FILE,'w') as json_file:
        return json.dump(contacts ,json_file)