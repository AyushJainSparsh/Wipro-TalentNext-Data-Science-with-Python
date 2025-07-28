# Write a program to check if a given number is Positive, Negative, or Zero

n=int(input("Enter a number: "))
if n > 0:
    print(f"{n} is a Positive number")
elif n < 0:
    print(f"{n} is a Negative number")
else:
    print(f"{n} is Zero")

# Write a program to check if a given number is odd or even.

n = int(input("Enter a number: "))
if n % 2 == 0:
    print(f"{n} is an Even number")
else:
    print(f"{n} is an Odd number")

# Given two non-negative values, print true if they have the same last digit, such as with 27 and 57.
# lastDigit(7, 17) → true                                                
# lastDigit(6, 17) → false
# lastDigit(3, 113) → true

def last_digit(a, b):
    return a % 10 == b % 10
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(last_digit(a, b))

# Write a program to print numbers from 1 to 10 in a single row with one tab space.
for i in range(1, 11):
    print(i, end='\t')

# Write a program to print even numbers between 23 and 57. Each number should be printed in a separate row.
for i in range(24, 58, 2):
    print(i)

# Write a program to check if a given number is prime or not.

n= int(input("Enter a number: "))
if n > 1:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print(f"{n} is not a prime number.")
            break
    else:
        print(f"{n} is a prime number.")

# Write a program to print prime numbers between 10 and 99.

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
for i in range(10, 100):
    if is_prime(i):
        print(i, end=' ')

# Write a program to print the sum of all the digits of a given number.
# Example:
# I/P:1234
# O/P:10

n = int(input("Enter a number: "))
sum_of_digits = sum(int(digit) for digit in str(n))
print(sum_of_digits)

'''
Write a program to reverse a given number and print.

Example:1
I/P: 1234
O/P:4321

Example:2
I/P:1004
O/P:4001
'''
n= int(input("Enter a number: "))
reversed_number = str(n)[::-1]
print(reversed_number)

'''
Write a program to find if the given number is palindrome or not

Example:1
I/P:110011
O/P: 110011 is a palindrome.

Example:2
I/P:1234
O/P: 1234 is not a palindrome.
'''

n = int(input("Enter a number:"))
reversed_number = str(n)[::-1]
reversed_number = int(reversed_number)
if n==reversed_number :
    print(f"{n} is a pallindrome.")
else:
    
    print(f"{n} is not a pallindrome.")