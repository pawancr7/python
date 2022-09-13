# n!=1 *2 * 3 * 4 ........*n
# n = 4


# factorial example
# product = 1
# for i in range(1):
#     product = product * (i+1)
# print(product)
'''
formula for factorial
 factorial (n) = n * factorial (n-1)
'''


'''def factorial_iter(n):

    product = 1
    for i in range(n):
        product = product * (i+1)
    return product


print(factorial_iter(4))
'''


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)


f = factorial(4)
print(f)
