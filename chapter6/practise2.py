sub1 = int(input("enter the marks "))
sub2 = int(input("enter the marks "))
sub3 = int(input("enter the marks "))

'''
if (sub1 > 33):  # and sub2 > 33 and sub3 > 33):
    print("passed in sub1  subject")
else:
    print("failed in sub1 subject")

if(sub2 > 33):
    print("passed in sub2 subject")
else:
    print("failed in sub2 subject ")

if(sub3 > 33):
    print("passed in sub3 subject")
else:
    print("failed in sub3 subject ")'''

if (sub1 < 33 or sub2 < 33 or sub3 < 33):
    print("you are failed  by one of subject is 33% ")
else:
    print("you are passed ")

if ((sub1 + sub2 + sub3)/3 * 100 < 40):
    print("great cleared exam")
else:
    print("failed in exam ")

'''
total = ((sub1 + sub2 + sub3) / 300 * 100)

if (total == 40 > 100):
    print("your total marks ", total)
else:
    print("you r fail ")
'''
