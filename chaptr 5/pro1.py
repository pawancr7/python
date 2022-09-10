mydict = {"kurchi": "chair",
          "dabba": "box",
          "vastu": "item"
          }
print("options are listed ", mydict.keys())
a = input("Enter the hindi word \n")
# print("the meaning of your word is : ", mydict[a])


print("the meaning of your word is : ", mydict.get(a))


word = {
    'pankha': 'fan',
    'kapda': 'cloth',
    'dakhan': 'cap'
}
print('options are ', word.keys())
w = input("enter the hindi word ")

# print(word[w])
print(word.get(w))  # this will not throw error
