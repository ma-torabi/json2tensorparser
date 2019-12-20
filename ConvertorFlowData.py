#!/usr/bin/python3

import json
import glob
import os

# Global Vaiables
vector = [[]]
keyname = ''
level = 0


# Recursive Function for Reading JSON Array
def getKeys( array, keyname, level, index):
    if hasattr(array, "__len__") and not isinstance(array, str):
        kname = ''

        for (k, v) in array.items():
            if keyname == '':
                kname  = k    
            else:
                kname  = keyname + '-' + k
            if not hasattr(v, "__len__") or isinstance(v, str):
                if (index == 1) and ('BF_label' not in kname):
                    vector[0].append(kname)
                # lable must not be in the vector
                if 'BF_label' not in kname :    
                    vector[index].append(v)
            level +=1 
            getKeys(v, kname, level,index)
    

# Main Funtion
def main():
    i = 0
    # Load json file(s)
    path = 'sample-data/'
    for filename in glob.glob(os.path.join(path, '*.json')):
        with open(filename, 'r') as f:
            array = json.load(f)
            
            if 'tuple' not in vector[0]:
                vector[0].append('tuple')

            for (key, value) in array.items():
                vector.append([])
                i += 1
                vector[i].append(key)

                # fill vector  per flow/packet information
                for (keytype, valuetype) in value.items():
                    level = 0
                    keyname = ''
                    #only check flow features
                    if (keytype == 'flow_features' or keytype == 'flow_metadata'):
                        getKeys(valuetype, keyname, level, i)
           

    new_path = 'sample-data/flow-result'
    flow_result = open(new_path,'w+')
    for row in vector:
        flow_result.write("%s\n" % row)


if __name__ == '__main__':
    main()