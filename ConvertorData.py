#!/usr/bin/python3

import json

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
                if index == 1:
                    vector[0].append(kname)
                vector[index].append(v)
            level +=1 
            # print(kname)
            getKeys(v, kname, level,index)
    

# Main Funtion
def main():
    # Load json file(s)
    with open('sample-data/1539866692_com.iconology.comics_MIRAGE-2019_traffic_dataset_labeled_biflows.json', 'r') as f:
        array = json.load(f)
    i = 0
    vector[i].append('tuple')

    for (key, value) in array.items():
        vector.append([])
        i += 1
        vector[i].append(key)
        # fill vector 
        # per flow/packet information
        for (keytype, valuetype) in value.items():
            level = 0
            keyname = ''
            print(keytype)
            #only check flow features
            if (keytype == 'flow_features' or keytype == 'flow_metadata'):
                getKeys(valuetype, keyname, level, i)
    # print(vector)

    new_path = 'sample-data/flow-result'
    flow_result = open(new_path,'w')
    for row in vector:
        flow_result.write("%s\n" % row)


if __name__ == '__main__':
    main()