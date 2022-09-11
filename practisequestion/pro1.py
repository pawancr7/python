'''num1 = int(input("enter the first numb"))
num2 = int(input("enter the  numbe2 "))
num3 = int(input("enter the  numbe3 "))
num4 = int(input("enter the  numbe4 "))
num5 = int(input("enter the  numbe5 "))
num6 = int(input("enter the  numbe6 "))
num7 = int(input("enter the  numbe7 "))
num8 = int(input("enter the  numbe8 "))

s = {num1, num2, num3, num4, num5, num6, num7, num8}
print(s)
'''

'''
S = {12, '12', 23.32, 'pawan'}
print(S)
'''


# size of sets is 2
s = set()
s.add(20)
s.add(20.0)  # if s.add(20.1) then size of sets is 3
s.add('20')
print(len(s))
