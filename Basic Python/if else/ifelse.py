a = 200
b = 33
c = 500
if b > a :
    print ("b is greater than a")
elif b == a:
    print ("a and b are equals")
else :
    print ("b is not greater than a")

#s ternary operator
print ("A") if a > b else print ("B")

# ternary operator 3 condition
print ("A") if a > b else print ("=") if a == b else print ("B")

# and 
if a > b and c > a:
    print ("Both condition are True")
else :
    print("At least one of the conditions is False")
# or
if a > b or a > c:
    print("At least one of the conditions is True")
else :
    print ("Both condition are False")
    
# not
if not b > a :
    print ("b is not greater than a")
else :
    print ("b is greater than a")

#nested if
x = 41
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

# pass
if x > 10 :
    pass





