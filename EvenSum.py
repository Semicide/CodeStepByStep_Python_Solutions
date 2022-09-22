#This program will sum the even numbers and print out their sum and max even number
def even_sum():
    t= int(input("how many integers? "))
    sum = 0
    max = 0 
    for i in range(t):
            num = int(input("next integer? "))
            if num % 2 == 0:
                 sum += num
                 if num > max:
                         max = num
    print("even sum =",sum)
    print("even max =", max)
