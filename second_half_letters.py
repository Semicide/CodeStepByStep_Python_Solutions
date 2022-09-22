#accepts a string as its parameter and returns an integer representing how many of letters in the string come from the second half of the alphabet
def second_half_letters(x):
    alphabet=["n","o","p","q","r","s","t","u","v","w","x","y","z"]
    a=x.lower()
    syc=0
    shl=0
    for i in range(len(a)):
        if(a[i] not in alphabet):
            syc +=1
        else:
            shl +=1
    return shl
