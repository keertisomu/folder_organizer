import os 
import json

def load_ext():
    with open('extensions.json') as extensions:
        data = json.load(extensions)
        return data
    
