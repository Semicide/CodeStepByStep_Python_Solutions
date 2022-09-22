#flips the lines in a poem in the question to make it look like the wanted text
def flip_lines(a):
    f = open(a)
    l = f.readlines()
    
    
    for i in range(0,len(l)-1,2):
        l[i],l[i+1] = l[i+1],l[i]
        
        print(l[i].upper(),end="")
        print(l[i+1].lower(),end="")

    if len(l) % 2 == 1:
        print(l[-1].upper())
