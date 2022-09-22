### accepts a string parameter and returns a new string with all consecutive occurrences of the same character
### in the string replaced by a single occurrence of that character
def remove_duplicates(x):
    x_list = list(x)
    i = 0
    while i < len(x_list)-1:
        if x_list[i] == x_list[i+1]:
            x_list.pop(i)
        else :
            i +=1
        
    a = ""
    for i in range(len(x_list)):
        a += x_list[i]
    return a
