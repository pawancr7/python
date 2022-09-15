# use open function to read the file content !
f = open("newtext.txt", "r")  # by default mode is r

data = f.read()
# we can also specify the number of character in read():f.read(2)
data = f.read(5)
print(data)
f.close()
