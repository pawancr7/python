# with statement is best way to open and close the file automatically


# with open('newtext.txt', 'r') as f:
#     a = f.read()


with open("anothertext.txt", "w") as f:
    a = f.write("memememmememme")

print(a)
