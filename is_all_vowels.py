#this code will return True if the string that eneterd in the last part is made with only vowels  otherwise it will return False
def is_all_vowels(s):
    vowels = 'AEIOUaeiou '
    count = 0
    for i in s:
        if(i in vowels):
            count +=1
    if(count==len(s)):
        return True
    else:
        return False
