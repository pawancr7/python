letter = '''Dear  NAME ,
            greating from ineuron . i am happy to inform you have made wonder fuull choice .
                     you are selected !
             <|DATE|>'''

name = input("Enter your name ")
date = input("enter your date ")
letter = letter.replace("NAME", name)
letter = letter.replace("<|DATE|>", date)
print(letter)
