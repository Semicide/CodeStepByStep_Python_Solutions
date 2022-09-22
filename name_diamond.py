# accepts a string as a parameter and prints it in a "diamond" format
def name_diamond(a):
    for i in range(len(a)):
        print(a[0:i])
    for i in range(len(a)):
        print((" " * i) + a[i:])
