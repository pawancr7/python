# sets
'''a = {1, 2, 2, 3, 4, 5, 6, 6, 7}
print(type(a))
print(a)
'''
# creating empty dictionary
a = {}
print(type(a))
print(a)


# creating a empty sets
'''b = set()
print(type(b))
'''

b = set()
b.add(23)
b.add(34)
b.add(3)
b.add(3)  # adding  a value repeatedly does not change sets
b.add((4, 3, 5, 6))
# b.add({2: 4}) you cant add dict to set
print(type(b))
print(b)

# sets are unindexed
# sets are unordered

# length of sets
print(len(b))


b.remove(23)  # removes 5 from sets
print(b)

print(b.pop())
print(b)
