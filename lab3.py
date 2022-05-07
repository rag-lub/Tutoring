def subset(setA, setB):
    return setB.issubset(setA) #issubset method compare if one set is a subset of another. The method is called on the set that is being checked if it is a subset, in this case setB.issubset(setA) means is setB a subset of set A. 
#print(subset({5,10,15,20,25},{1,2,3}))
def list_of_tuples_dictionary(lst):
    output_dct = {} #creates empty dictionary
    for elem in lst: # loops through the input list of tupples, elen is assigned a single tupple for each loop execution that looks like this (value0, value1)
        output_dct.update({elem[0]:elem[1]}) # creates a key-value pair and adds it to the dictionary, elem[0] and elem[1] refer to value0 and value1 in the tupple and assigns them as key value pair by putting the ":" between them and wrapping them in {}
    return output_dct #returns the dictionary after the loop has ended updating it
#print(list_of_tuples_dictionary([('apple','sweet'),('num',55),('bool',True),(99.4,103)]))
        
def lists_to_dictionary(lstA,lstB):
    output_dct = {} #creates empty dictionary
    for i in range(len(lstA)): # loops through the index of lstA
        output_dct.update({lstA[i]:lstB[i]}) # creates a key-value pair and adds it to the dictionary, lstA[i] and lstB[i] refer to the elements at i-th position in lstA and lstB respectively and assigns them as key-value pair by putting the ":" between them and wrapping them in {}
    return output_dct #returns the dictionary after the loop has ended updating it
#print(lists_to_dictionary(['car','color','year'],['mazda','blue','2005']))
def unique_values(d):
    return list(set(d.values())) # values() dictionarry method returns a list of all values in the dictionary, creating a set out of them eliminates duplicates and finally converting it back to list satisfies the question requirements for a list output
#print(unique_values({'a':1,'b':2,'c':3,'d':2,'e':1}))
def combine_dictionaries1(dictA,dictB):
    newDict={} #create blank new dictionary, will be used to store combined dictA and dictB
    keysAlst = list(dictA.keys()) # create a list of dictA keys and store it in keysA list
    keysBlst = list(dictB.keys()) # create a list of dictB keys and store it in keysB list
   
    for i in range(len(keysAlst)): # create a loop over the index of keysA, this is done so we care refer to keys from both dictA and dictB by index
        if keysAlst[i] not in newDict.keys(): # this checks if the key at i-th position from dictA keys stored in keysAlst exists in the new dictionary
            newDict[keysAlst[i]] = dictA[keysAlst[i]] #if it doesn't, it inserts the key in the new dictionary (newDict[keysAlst[i]]) and assigns the key's corresponding value from dictA (dictA[keysAlst[i]])
        else: #if the key exists in the dictionary, it already has a corresponding value as well
            multi_valuesLst = [] #this creates a temporary list to store the existing value for the key from newDict
            multi_valuesLst.append(newDict[keysAlst[i]])# the existing value is stored in the temporary list
            multi_valuesLst.append(dictA[keysAlst[i]]) # the key's value from dictA is also stored in the temp list
            newDict[keysAlst[i]] = multi_valuesLst # finally the key's value in newDict is update to the temp list which contains both values for the key
            # The next if statement does exactly the same checkes and steps for dictB. It checks if a key exists in newDict.
            # if it doesn't, the key-value pair from dictB is inserted into newDict
            # if it does, it stores the existing value from newDict into a temp list (multi_valuesLst), adds the key's value from dictB and finally updates the key's value in newDict to the temp list of values
        if keysBlst[i] not in newDict.keys(): 
            newDict[keysBlst[i]] = dictB[keysBlst[i]]
        else:
            multi_valuesLst = []
            multi_valuesLst.append(newDict[keysBlst[i]])
            multi_valuesLst.append(dictB[keysBlst[i]])
            newDict[keysBlst[i]] = multi_valuesLst
    return newDict
def combine_dictionaries(dictA,dictB):
   newDict = dict()
   for d in [dictA,dictB]:
    for key in d:
        if key in newDict:
            newDict[key] += (d[key])
        else:
            newDict[key] = d[key]

def subset(setA, setB):
    print(setA.intersection(setB)) 
    if setA.intersection(setB):
        return True
    else:
        return False
print(subset({1,2,3,4,5},{2,3}))
#print(combine_dictionaries({'number':[1,2,3]},{'number':456}))
