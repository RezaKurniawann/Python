'''
Sets are unordered, so cannot be sure in which order the items will apppear
Sets cannot have two items with the same value

Method	                    Shortcut	        Description
add()	 	                                    Adds an element to the set
clear()	 	                                    Removes all the elements from the set
copy()	 	                                    Returns a copy of the set
difference()	                -	            Returns a set containing the difference between two or more sets
difference_update()	            -=	            Removes the items in this set that are also included in another, specified set
discard()	 	                                Remove the specified item
intersection()	                &	            Returns a set, that is the intersection of two other sets
intersection_update()	        &=	            Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	 	                            Returns whether two sets have a intersection or not
issubset()	                    <=	            Returns whether another set contains this set or not
 	                            <	            Returns whether all items in this set is present in other, specified set(s)
issuperset()	                >=	            Returns whether this set contains another set or not
 	                            >	            Returns whether all items in other, specified set(s) is present in this set
pop()	 	                                    Removes an element from the set
remove()	 	                                Removes the specified element
symmetric_difference()	        ^	            Returns a set with the symmetric differences of two sets
symmetric_difference_update()	^=	            Inserts the symmetric differences from this set and another
union()	                        |	            Return a set containing the union of sets
update()	                    |=	            Update the set with the union of this set and others
''' 
def fruitFunction () :
    fruitSet = {"apple", "banana", "cherry"}
    return fruitSet
thisSet = {"apple", "banana", "cherry", True, 1, 2} # True and 1 is considered the same value in sets
print ("1.",thisSet)

thisSet = {"apple", "banana", "cherry", False, True, 0} # False and 0 is considered the same value in sets
print("2.",thisSet)

print ("\nGet length")
fruitSet = fruitFunction ()
print (len (fruitSet))

print ("\nContain different data types")
set1 = {"abc", 34, True, 40, "male"}
print (set1)

print ("\nGet Type")
print (type(fruitSet))

print ("\nSet Constructor")
fruitSet = set (("apple", "banana", "cherry"))
print (fruitSet)

print ("\nAcces items")
fruitSet = fruitFunction ()
for i in fruitSet :
    print (i)
print ()

print ("is 'banana' in 'fruitSet' :", "banana" in fruitSet)
print ("is 'banana' not in 'fruitSet' :", "banana" not in fruitSet)

print ("\nAdd items")
fruitSet.add ("orange")
print ("1.",fruitSet)
tropical = {"pineapple", "mango", "papaya"}
fruitSet.update (tropical)
print ("2.", fruitSet)
fruitList = ["kiwi", "orange"]
fruitSet.update(fruitList)
print("3.",fruitSet)

print ("\nRemove items")
fruitSet = fruitFunction ()
fruitSet.remove ("banana")
print ("1.", fruitSet)
fruitSet = fruitFunction ()
fruitSet.discard("banana")
print ("2.",fruitSet)
fruitSet = fruitFunction ()
x = fruitSet.pop()
print ("3.", x, fruitSet)
fruitSet = fruitFunction ()
fruitSet.clear()
print ("4.",fruitSet)
fruitSet = fruitFunction ()
del fruitSet

print ("\nLoop")
fruitSet = fruitFunction ()
for i in fruitSet :
    print (i)

print ("\nJoin Sets")
#union
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print("1.", set3)
# can use | instead of the union ()
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1 | set2
print("2.", set3)

#join multiple sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1.union(set2, set3, set4)
print("3.",myset)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1 | set2 | set3 |set4
print("4.",myset)

# join set and tuple
x = {"a", "b", "c"}
y = (1, 2, 3)
z = x.union(y)
print("5",z)

#update
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print("6.",set1)

#intersection
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print("7.",set3)

# can use & instead of the intersection ()
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 & set2
print("8.",set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.intersection_update(set2)
print("9.",set1)

set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}
set3 = set1.intersection(set2)
print("10.",set3)

#difference ()
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print("11.", set3)

#can use - instead of the difference ()
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 - set2
print("12.",set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.difference_update(set2)
print("13.", set1)

#symmetric differences
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
print("14.",set3)

# use ^ instead of the symmetric_difference ()
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 ^ set2
print("15.",set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.symmetric_difference_update(set2)
print("16.",set1)














