#prompts for the name of, and then reads, a file of data about the number of hours worked by several employees. 
#Each line begins with the employee's ID number, followed by their name, then a sequence of numbers representing how many hours they worked each day. For example:
# 123 Amy 12.5 8.5 7.25 3.25
# 456 Miles 4.0 11.6 6.5 12.2 2.7
# 802 Jessie 1.5
# 647 Vilde 8.0 3.5 6.5
def hours():
    x = input("Input file? ")
    file = open(x)
    lines = file.readlines()
    for line in lines:
        part = line.split()
        id = part[0]
        name = part[1]
        sum = 0
        t = 0
        for i in range(2, len(part)):
            sum += float(part[i])
            t += 1
        average = sum / t
        print(name + " (ID#" + id + ") worked " + str(round(sum, 1)) + " hours (" + str(round(average, 1)) + "/day)")
