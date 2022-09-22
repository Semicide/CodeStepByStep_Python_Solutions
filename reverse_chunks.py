#This function  accepts a string y and integer x  
#as parameters and returns a new string that reverses the relative order of every x characters of y
def reverse_chunks(y, x):
    empty = ''
    i = 0
    while i + x <= len(y):
       slice = y[i:i+x]
       empty += slice[::-1]
       i += x
    j = len(y) % x
    if j!= 0:
        empty += y[-j:]
    return empty
