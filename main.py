from typing import Dict, Any


def waluta_dict_na_str(dictionary):
    
    sentence = ""
    
    tableKeys = list(dictionary.keys())
    
    tableVals = []
    for value in dictionary.values():
        tableVals.append(int(value))
    
    for i in range(len(tableVals)):
        if tableVals[i] != 0:
            if i == 0 or i ==2:
                sentence += str(tableVals[i]) + " " + tableKeys[i] + "y "
            else:
                sentence += str(tableVals[i]) + " " + tableKeys[i] + "e "
        else:
            sentence += ""

    return sentence    

waluta_dict_na_str()

