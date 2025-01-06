'''
Method	        Description
clear()	        Removes all the elements from the dictionary
copy()	        Returns a copy of the dictionary
fromkeys()	    Returns a dictionary with the specified keys and value
get()	        Returns the value of the specified key
items()	        Returns a list containing a tuple for each key value pair
keys()	        Returns a list containing the dictionary's keys
pop()	        Removes the element with the specified key
popitem()	    Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	    Updates the dictionary with the specified key-value pairs
values()	    Returns a list of all the values in the dictionary
'''

def dictionaryFunction ():
    thisDict = {
        "brand" : "Ford",
        "model" : "Mustang",
        "year"  : 1946
    }
    return thisDict

thisDict = dictionaryFunction ()
print ("1.", thisDict)
print ("2.", thisDict["brand"])

#duplicate not allowed
thisDict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print("3.", thisDict)

#length
print ("4.",len(thisDict))

#type
print ("5.", type(thisDict))

#dictionary constructor
thisDict = dict (name = "John", age = 36, country = "Norway")
print ("6.", thisDict)


print ("\nAcces Items")
thisDict = dictionaryFunction ()
x = thisDict["model"]
print ("1.",x)
x = thisDict.get("model")
print("2.", x)

print("\nGet Keys")
x = thisDict.keys()
print ("1.",x) #before change
thisDict ["color"] = "white"
print ("2.", x) #after change

print ("\nGet Values")
thisDict = dictionaryFunction ()
x = thisDict.values()
print ("1.",x) #before change
thisDict["year"] = 2020
print ("2.",x) #after change

print("\nGet Items")
thisDict = dictionaryFunction ()
x= thisDict.items ()
print ("1",x) #before change
thisDict["year"] = 2020
print ("2.",x) #after change

print ("\nCheck if key exist")
if "model" in thisDict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")
else :
    print("No, 'model' is not one of the keys in the thisdict dictionary")

print ("\nChange Dictionary")
thisDict = dictionaryFunction ()
thisDict["year"] = 2019
print ("1.",thisDict)
thisDict.update({"year" : 2020})
print ("2.",thisDict)

print ("\nAdd Items")
thisDict = dictionaryFunction ()
thisDict["color"] = "white"
print ("1.",thisDict)
thisDict.update({"color" : "red"})
print ("2.",thisDict)

print ("\nRemoving List")
thisDict = dictionaryFunction ()
thisDict.pop("model")
print ("1.", thisDict)
thisDict = dictionaryFunction ()
thisDict.popitem() #last insert
print ("2.", thisDict)
thisDict = dictionaryFunction ()
del thisDict ["model"]
print ("3.", thisDict)
del thisDict 
# print (thisDict) - this will cause an eror because thisDict no longer exits
thisDict = dictionaryFunction ()
thisDict.clear()
print ("4.", thisDict) # empty dictionary

print ("\nLoop")
thisDict = dictionaryFunction ()
for x in thisDict:
    print (x) # return key

print ()
for x in thisDict.keys():
    print (x) #return keys

print ()
for x in thisDict:
    print(thisDict[x]) #return values

print ()
for x in thisDict.values():
    print (x) #return values 

print ()
for x, y in thisDict.items():
    print (x, y) # return key and values

print("\nCopy Dictionary")
newDict = thisDict.copy()
print ("1.",newDict)

thisDict = dictionaryFunction ()
newDict = dict (thisDict)
print ("2.", newDict)

print ("\nNested Dictionary")
myFamily = {
  "child1" : {
    "name" : "Raihan",
    "year" : 2001
  },
  "child2" : {
    "name" : "Reza",
    "year" : 2004
  },
  "child3" : {
    "name" : "Rezky",
    "year" : 2009
  }
}
print ("1.",myFamily)
print ("2.",myFamily["child1"]["name"])

print ("\nnested loop dictionary")
for x, obj in myFamily.items():
    print (x)
    for y in obj:
        print (y + ":", obj[y])










