import json
import sys 
import base64

args = sys.argv

def btoa(string):
    encoded_string = base64.b64encode(string.encode()).decode()
    return encoded_string

def atob(encoded_string):
    decoded_string = base64.b64decode(encoded_string).decode()
    return decoded_string

def load():
    with open('/root/.xdb/.json', 'r', encoding='utf-8') as file:
        return json.load(file)
    
def save(data):
    with open('/root/.xdb/.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False) 

def add(key,value):
    data = load()
    data[btoa(key)] = btoa(value)
    save(data)

def get(key):
    data = load()
    key = btoa(key)
    if key in data:
        return atob(data[btoa(key)])
    else:
        return ':('

def update(key,value):
    data = load()
    data[btoa(key)] = btoa(value)
    save(data)

def delete(key):
    data = load()
    key = btoa(key)
    if key in data:
        del data[key]
        save(data)
    else:
        print('Already deleted (?)')

if args[1] == 'add' and len(args) == 4:
    add(args[2],args[3])

elif args[1] == 'get' and len(args) == 3:
    print(get(args[2]))

elif args[1] == 'update' and len(args) == 4:
    update(args[2],args[3])

elif args[1] == 'delete' and len(args) == 3:
    delete(args[2])
