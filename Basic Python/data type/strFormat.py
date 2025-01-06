#f-strings
txt = f"The price is 49 dollars"
print ("1.",txt)

#placeholders and modifiers
price = 59
txt = f"The price is {price} dollars"
print ("2.", txt)

txt = f"The price is {price:.2f} dollars"
print ("3.", txt) 

txt = f"The price is {95:.2f} dollars"
print ("4.", txt)

#perform operations 
txt = f"The price is {20*59} dollars"
print ("5.",txt)

price = 59
Tax = 0.25
txt = f"The price is {price + (price * Tax)} dollars"
print ("6.", txt)

#if else
price = 49
txt =f"The price is {'Expensive' if price > 50 else 'Cheap'}"
print ("7.", txt)

#execute function
fruit = "apple"
txt = f"I love {fruit.upper()}"
print ("8.",txt)

def myConverter (x):
    return x * 0.3048

txt = f"The plane is flying at a {myConverter(30000)} meter altitude"
print ("9.", txt)

# use a comma as a thousand separator
price = 59000
txt = f"The price is {price:,} dollars"
print ("10.", txt)

#more formating types

print ()

value = 1234.56789
# Left align
print(f"{value:<20}")  # '1234.56789           '

# Right align
print(f"{value:>20}")  # '           1234.56789'

# Center align
print(f"{value:^20}")  # '     1234.56789     '

# Place sign to the left most position
print(f"{value:=+20}")  # '+           1234.56789'
print(f"{-value:=+20}") # '-           1234.56789'

# Plus sign for positive numbers
print(f"{value:+}")    # '+1234.56789'
print(f"{-value:+}")   # '-1234.56789'

# Space for positive numbers
print(f"{value: }")    # ' 1234.56789'
print(f"{-value: }")   # '-1234.56789'

# Comma as thousand separator
print(f"{value:,}")    # '1,234.56789'

# Underscore as thousand separator
print(f"{value:_}")    # '1_234.56789'

# Binary format
print(f"{255:b}")      # '11111111'

# Unicode character
print(f"{65:c}")       # 'A'

# Decimal format
print(f"{value:.2f}")  # '1234.57'

# Scientific format (lower case e)
print(f"{value:e}")    # '1.234568e+03'

# Scientific format (upper case E)
print(f"{value:E}")    # '1.234568E+03'

# Fixed point format
print(f"{value:.2f}")  # '1234.57'

# Fixed point format (upper case for inf and nan)
print(f"{float('inf'):F}")  # 'INF'

# General format
print(f"{value:g}")    # '1234.57'

# General format (upper case E for scientific notation)
print(f"{value:G}")    # '1234.57'

# Octal format
print(f"{255:o}")      # '377'

# Hex format (lower case)
print(f"{255:x}")      # 'ff'

# Hex format (upper case)
print(f"{255:X}")      # 'FF'

# Number format
print(f"{value:n}")    # '1234.57'

# Percentage format
print(f"{0.1234:%}")   # '12.340000%'
