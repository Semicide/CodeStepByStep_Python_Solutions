#accepts a string parameter returns a new string replacing each of its characters with two consecutive copies of that character
def stutter(stre):
    i = 0
    s=""
    while i < len(stre):

        s = s+stre[i]+stre[i]
        i+=1
    return s
