def plus (*args):
    result = 0
    for data in args:
        result += data
    return result

def minus(*args):
    
    result = args[0] 
    for data in args[1:]:
        result -= data
    
    return result

def times (*args):
    result = 1
    for data in args:
        result *= data
    return result


def devided (*args):
    result = args[0]
    for data in args [1:]:
        result /= data
    return result

def powersofnumbers (n:int):
    return lambda angka: angka**n
    