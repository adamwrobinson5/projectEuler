# #Project Euler

import math

# # ***** PROBLEM 1 *****
# # If we list all the natural numbers below 10 that are multiples 
# # of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# # Find the sum of all the multiples of 3 or 5 below 1000.

# print ''
# print '*** PROBLEM 1 ***'
# print ''
# arr = []
# sum = 0
# for x in range(1,1000):
#     if (x % 3 == 0 or x % 5 == 0):
#         arr.append(x)
#         sum += x
# print 'ANSWER: ' + str(sum)




# # ***** PROBLEM 2 *****
# # Each new term in the Fibonacci sequence is generated by adding the
# # previous two terms. By starting with 1 and 2, the first 10 terms 
# # will be: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# # By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

# print ''
# print '*** PROBLEM 2 ***'
# print ''
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
# print 'ANSWER: ' + str(sumEven)




# # ***** PROBLEM 3 *****
# # The prime factors of 13195 are 5, 7, 13 and 29.
# # What is the largest prime factor of the number 600851475143?

# print ''
# print '*** PROBLEM 3 ***'
# print ''
# primeArray = []
# x = 600851475143
# for i in range(3,int(math.sqrt(x))):
#     while x % i == 0:
#         primeArray.append(i)
#         x = x/i
# print 'ANSWER: ' + str(primeArray[-1])




# # ***** PROBLEM 4 *****
# # A palindromic number reads the same both ways. The largest
# # palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.
# # Find the largest palindrome made from the product of two 3-digit numbers.

# print ''
# print '*** PROBLEM 4 ***'
# print ''
# a = 999
# b = 999
# palArray = []
# while b >= 100:
#     a = 999
#     while a >= 100:
#         front = []
#         back = []
#         revBack = []
#         mult = a * b
#         num = str(mult)
#         if len(num) == 6:
#             for i in range(0, 3):
#                 front.append(int(num[i]))
#             for j in range(3, 6):
#                 back.append(int(num[j]))
#             revBack.append(back[2])
#             revBack.append(back[1])
#             revBack.append(back[0])
#             if cmp(front, revBack) == 0:
#                 palArray.append(mult)
#         a -= 1
#     b -= 1
# sort = sorted(palArray)
# largestPalindrome = sort[-1]
# print 'ANSWER: ' + str(largestPalindrome)




# # ***** PROBLEM 5 *****
# # 2520 is the smallest number that can be divided by each of the numbers 
# # from 1 to 10 without any remainder. What is the smallest positive number 
# # that is evenly divisible by all of the numbers from 1 to 20?

# print ''
# print '*** PROBLEM 5 ***'
# print ''
# num = 1
# primeArray = []
# for x in range(2,21):
#     primeCheck = 0
#     for y in range(2, x+1):
#         if x % y != 0:
#             primeCheck += 1
#         elif x != 2:
#             break
#         if primeCheck == x-2 or x == 2:
#             pwr = 1
#             exp = 0
#             while exp < 20:
#                 exp = x**pwr
#                 primeArray.append(x)
#                 pwr += 1
#             primeArray.remove(x)
#             break
# for i in range(0, len(primeArray)):
#     num *= primeArray[i]
# print 'ANSWER: ' + str(num)




# # ***** PROBLEM 6 *****
# # The sum of the squares of the first ten natural numbers is,
# # 1**2 + 2**2 + ... + 10**2 = 385
# # The square of the sum of the first ten natural numbers is,
# # (1 + 2 + ... + 10)**2 = 552 = 3025
# # Hence the difference between the sum of the squares of the 
# # first ten natural numbers and the square of the sum is 
# # 3025 - 385 = 2640
# # Find the difference between the sum of the squares of the 
# # first one hundred natural numbers and the square of the sum.

# print ''
# print '*** PROBLEM 6 ***'
# print ''
# natSum = 0
# natSqr = 0
# for x in range(1,101):
#     natSum += x**2
# for x in range(1,101):
#     natSqr += x
# natSqr **= 2
# diff = natSqr - natSum
# print 'ANSWER: ' + str(diff)




# # ***** PROBLEM 7 *****
# # By listing the first six prime numbers: 
# # 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# # What is the 10001st prime number?

# print ''
# print '*** PROBLEM 7 ***'
# print ''
# primeArray = [2]
# n = 110000
# check = 0
# done = False
# for x in range(2, n):
#     for y in range(2, x):
#         if x % y == 0:
#             break
#         else:
#             check += 1
#         if check == (x-2):
#             primeArray.append(x)
#         if len(primeArray) == 10001:
#             done = True
#             break
#     if done == True:
#         break
#     check = 0
# print primeArray[-1]




# # ***** PROBLEM 8 *****
# # The four adjacent digits in the 1000-digit number that 
# # have the greatest product are 9 * 9 * 8 * 9 = 5832
# # Find the thirteen adjacent digits in the 1000-digit number 
# # that have the greatest product. What is the value of this product?

# print ''
# print '*** PROBLEM 8 ***'
# print ''
# product = 0
# greatestProduct = 0
# number = str(7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450)
# for x in range(0,988):
#     product = int(number[x]) * int((number[x+1])) * int((number[x+2])) * int((number[x+3])) * int((number[x+4])) * int((number[x+5])) * int((number[x+6])) * int((number[x+7])) * int((number[x+8])) * int((number[x+9])) * int((number[x+10])) * int((number[x+11])) * int((number[x+12]))
#     if product > greatestProduct:
#         zero = number[x]
#         one = number[x + 1]
#         two = number[x + 2]
#         three = number[x + 3]
#         four = number[x + 4]
#         five = number[x + 5]
#         six = number[x + 6]
#         seven = number[x + 7]
#         eight = number[x + 8]
#         nine = number[x + 9]
#         ten = number[x + 10]
#         eleven = number[x + 11]
#         twelve = number[x + 12]
#         greatestProduct = product
# print 'zero: ' + str(zero)
# print 'one: ' + str(one)
# print 'two: ' + str(two)
# print 'three: ' + str(three)
# print 'four: ' + str(four)
# print 'five: ' + str(five)
# print 'six: ' + str(six)
# print 'seven: ' + str(seven)
# print 'eight: ' + str(eight)
# print 'nine: ' + str(nine)
# print 'ten: ' + str(ten)
# print 'eleven: ' + str(eleven)
# print 'twelve: ' + str(twelve)
# print greatestProduct




# # ***** PROBLEM 9 *****
# # A Pythagorean triplet is a set of three natural numbers, a < b < c, 
# # for which, a**2 + b**2 = c**2
# # For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.
# # There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# # Find the product a * b * c.

# print ''
# print '*** PROBLEM 9 ***'
# print ''
# def triplet():
#     done = False
#     for c in range(3,1000):
#         for b in range(2, c):
#             for a in range(1, b):
#                 sum = a + b + c
#                 if sum > 1000:
#                     break
#                 if sum == 1000:
#                     if a**2 + b**2 == c**2:
#                         triplet = a * b * c
#                         done = True
#                     if done == True:
#                         print 'end a: ' + str(a)
#                         print 'end b: ' + str(b)
#                         print 'end c: ' + str(c)
#                         print 'triplet: ' + str(triplet)
#                         return
# triplet()




# # ***** PROBLEM 10 *****
# # The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# # Find the sum of all the primes below two million.

print ''
print '*** PROBLEM 10 ***'
print ''
