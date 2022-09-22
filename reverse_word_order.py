#Takes a string prarameter s and reverses only its word order
def reverse_word_order(s):
        words = s.split(' ')
        rev = ' '.join(reversed(words))
        return rev
