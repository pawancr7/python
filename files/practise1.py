f = open('po.txt')
t = f.read()
if "twinkle" in t:
    print("present in poem")
else:
    print("not present in poem ")
f.close()
