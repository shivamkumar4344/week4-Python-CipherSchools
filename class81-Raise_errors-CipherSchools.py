def add(a,b):
    if(type(a) is int) and (type(b) is int):
        return a+b
    else:
        raise TypeError("Wrong type of data type...")
print(add('2','4'))


