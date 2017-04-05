#!/usr/bin/python2

def init(data):
    'initialize dict data'
    data['first'] = {}
    data['middle'] = {}
    data['last'] = {}

def store(data, name):
    'store name into data'
    partition = ['first','middle','last']
    full_name = name.split()
    if len(name) == 2:
        full_name.insert(1,"")
    for label,part in zip(partition, full_name):
        data[label].setdefault(part,[]).append(name)
    
def lookup(data, typ, name):
    'get full name whose first/middle/last  is name'
    return data[typ].get(name,None)

if __name__ == "__main__":
    notebook = {}
    init(notebook)
    store(notebook, 'bian ming liang')
    first = lookup(notebook, 'first', 'bian')
    middle = lookup(notebook, 'middle', 'ming')
    last = lookup(notebook, 'last', 'liang')
    final = lookup(notebook, 'last', '')
    print first, middle, last, "final :%r:"%final

