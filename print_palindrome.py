#To find out if a word is palindrome or not
def print_palindrome():

    text = input("Type one or more words: ")
    text_low = text.lower()
    x = -1
    
    for i in range(len(text_low)//2):
        if text_low[i] != text_low[x]:
            print(text,"is not a palindrome.")
            break
        if i == len(text_low)//2-1:
            print(text,"is a palindrome!")
        x -=1
print_palindrome()
