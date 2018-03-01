#Project Euler

import math

# ***** PROBLEM 1 *****
# If we list all the natural numbers below 10 that are multiples 
# of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

# print('***** PROBLEM 1 *****')
# arr = []
# sum = 0
# for x in range(1,1000):
#     if (x % 3 == 0 or x % 5 == 0):
#         arr.append(x)
#         sum += x
# print sum




# ***** PROBLEM 2 *****
# Each new term in the Fibonacci sequence is generated by adding the
# previous two terms. By starting with 1 and 2, the first 10 terms 
# will be: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

# print('***** PROBLEM 2 *****')
# fibArr = [1,2]
# evenArr = [2]
# sumEven = 2
# add = 0
# x = 2
# while add < 4000000:
#     add = fibArr[x-1] + fibArr[(x-2)]
#     if add % 2 == 0:
#         evenArr.append(add)
#         sumEven += add
#     fibArr.append(add)
#     x += 1
# fibArr.remove(add)
# print sumEven




# ***** PROBLEM 3 *****
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?

# print('***** PROBLEM 3 *****')
# primeArray = []
# x = 600851475143
# for i in range(3,int(math.sqrt(x))):
#     while x % i == 0:
#         primeArray.append(i)
#         x = x/i
# print primeArray[-1]




# ***** PROBLEM 4 *****
# A palindromic number reads the same both ways. The largest
# palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

print('***** PROBLEM 4 *****')
a = 999
b = 999
palArray = []
while b >= 100:
    a = 999
    while a >= 100:
        front = []
        back = []
        revBack = []
        mult = a * b
        num = str(mult)
        if len(num) == 6:
            for i in range(0, 3):
                front.append(int(num[i]))
            for j in range(3, 6):
                back.append(int(num[j]))
            revBack.append(back[2])
            revBack.append(back[1])
            revBack.append(back[0])
            if cmp(front, revBack) == 0:
                palArray.append(mult)
        a -= 1
    b -= 1
sort = sorted(palArray)
largestPalindrome = sort[-1]
print largestPalindrome