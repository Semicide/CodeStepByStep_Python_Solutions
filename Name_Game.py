#This program prints the following rhyme about the person's first and last name.
def game(name):
    print("{0}, {0}, bo-B{1}".format(name, name[1:]))
    print("Banana-fana fo-F{}".format(name[1:]))
    print("Fee-fi-mo-M{}".format(name[1:]))
    print("{}!".format(name.upper()))
    print()
    
first, last = [word for word in input("What is your name? ").split()]
game(first)
game(last)
