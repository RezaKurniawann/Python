'''
"List" is a collection which is ordered and changeable. Allows duplicate members.
"Tuple" is a collection which is ordered and unchangeable. Allows duplicate members.
"Set" is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
"Dictionary" is a collection which is ordered** and changeable. No duplicate members.
'''

carList = ["Ford", "Volvo", "BMW" ]
#acces items
x = carList [0]
print("1.",x)
#length
x = len(carList)
print("2.",x)
#loop
print ("3. Loop")
for x in carList:
    print(x)
#Append
carList.append("Honda")
print ("4.",carList)
#removing
carList.pop(1)
print ("5.", carList)
carList.remove("BMW")
print ("6.", carList)

'''
Method	    Description
append()	Adds an element at the end of the list
clear()	    Removes all the elements from the list
copy()	    Returns a copy of the list
count()	    Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	    Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	    Removes the element at the specified position
remove()	Removes the first item with the specified value
reverse()	Reverses the order of the list
sort()	    Sorts the list
'''

