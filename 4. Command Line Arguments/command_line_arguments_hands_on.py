# Write a program to accept two numbers as command line arguments and display their sum.

import sys
def sum_of_numbers():
    if len(sys.argv) != 3:
        print("Please provide exactly two numbers.")
        return
    
    try:
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])
        total = num1 + num2
        print(f"The sum of {num1} and {num2} is: {total}")
    except ValueError:
        print("Please provide valid numbers.")
sum_of_numbers()

# Write a program to accept a welcome message through command line arguments and display the file name along with the welcome message.

import sys
def welcome_message():
    if len(sys.argv) < 2:
        print("Please provide a welcome message.")
        return
    
    message = " ".join(sys.argv[1:])
    print(f"File Name: {sys.argv[0]}")
    print(f"Welcome Message: {message}")
welcome_message()

# Write a program to accept 10 numbers through command line arguments and calculate the sum of prime numbers among them.

import sys
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def sum_of_primes():
    if len(sys.argv) != 11:
        print("Please provide exactly 10 numbers.")
        return
    
    prime_sum = 0
    for arg in sys.argv[1:]:
        try:
            num = int(arg)
            if is_prime(num):
                prime_sum += num
        except ValueError:
            print(f"'{arg}' is not a valid number.")
    
    print(f"The sum of prime numbers is: {prime_sum}")
sum_of_primes()

