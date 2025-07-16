# Write a function to return the sum of all numbers in a list.  
# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20

def sum_of_list(list1):
    return sum(list1)
list1 = [8, 2, 3, 0, 7]
print("Sum of list:", sum_of_list(list1))

# Write a function to return the reverse of a string.  
# Sample String : "1234abcd"
# Expected Output : "dcba4321"

def reverse_string(s):
    return s[::-1]  
s = "1234abcd"
print("Original string:", s)
print("Reversed string:", reverse_string(s))

# Write a function to calculate and return the factorial of a number (a non-negative integer)

def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

n = 5
print("Factorial of", n, "is:", factorial(n))

# Write a function that accepts a string and prints the number of upper case letters and lower case letters in it.

def count_case(s):
    upper_count = sum(1 for c in s if c.isupper())
    lower_count = sum(1 for c in s if c.islower())
    return upper_count, lower_count
s = input("Enter a string: ")
upper_count, lower_count = count_case(s)
print("Upper case letters:", upper_count)
print("Lower case letters:", lower_count)

# Write a function to print the even numbers from a given list. List is passed to the function as an argument. 
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Result : [2, 4, 6, 8]

def even_numbers_from_list(lst):
    return [num for num in lst if num % 2 == 0]

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Even numbers from the list:", even_numbers_from_list(lst))

# Write a function that takes a number as a parameter and checks whether the number is prime or not

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input("Enter a number to check if it is prime: "))
if is_prime(n):
    print(n, "is a prime number.")
else:
    print(n, "is not a prime number.")