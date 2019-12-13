#!/usr/bin/python3

import json

with open('test.json', 'r') as f:
    array = json.load(f)


vector = [[],[]]
keyname = ''
level = 0
def getKeys( array, keyname, level):
    if hasattr(array, "__len__"):
        kname = ''
        for (k, v) in array.items():
            
            if keyname == '':
                kname  = k    
            else:
                kname  = keyname + '-' + k
            if not hasattr(v, "__len__"):
                vector[0].append(kname)
                vector[1].append(v)


            level +=1 
            getKeys(v, kname, level)
        

getKeys(array, keyname, level)
print(vector)