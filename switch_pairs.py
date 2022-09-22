#accepts a string as a parameter and returns that string with each pair of neighboring letters reversed.
# If the string has an odd number of letters, the last letter should not be modified.
def switch_pairs(ex):
    a = ''
    t = 0
    if len(ex) < 2:
        return ex
    while t < len(ex) - 1:
        a += ex[t + 1]
        a += ex[t]
        t += 2
    if len(ex) % 2 != 0:
        a += ex[-1]
    return a
