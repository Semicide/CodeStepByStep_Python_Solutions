#This code will only count the even numbers and will print their averages
def Average():
  y = int(input("Integer? "))
    x = 0
    i = 0
    a = 0
    while y != 0:
        if y % 2 == 0:
            x += y
            i += 1
            if (i != 0):
                a = float(x / i)
        y = int(input("Integer? "))
    return print ("Average: " + str(a))
    Average()
