#  the meaning of strip to remove the blank spaces from the string

'''
the = "       best player in the world     "
print(the)
print(the.strip())

'''


def remove(string, word):
    new_str = string.replace(word, "")
    return new_str.strip()


this = '        dog is a faithfull      '
n = remove(this, 'harry')
print(n)
