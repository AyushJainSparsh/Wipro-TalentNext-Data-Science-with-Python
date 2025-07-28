# Write a program to accept two numbers from the user and perform division. If any exception occurs, print an error message or else print the result

a = input("Enter first number: ")
b = input("Enter second number: ")
try:
    result = int(a) / int(b)
    print(f"The result of division is: {result}")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Please enter valid numbers.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Write a program to accept a number from the user and check whether it’s prime or not. If user enters anything other than number, 
# handle the exception and print an error message.

n = int(input("Enter a number to check if it's prime: "))
try:
    if n < 2:
        print(f"{n} is not a prime number.")
    else:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                print(f"{n} is not a prime number.")
                break
        else:
            print(f"{n} is a prime number.")
except ValueError:
    print("Error: Please enter a valid integer.")

# Write a program to accept the file name to be opened from the user, if file exist print the contents of the file in title case or 
# else handle the exception and print an error message.

file_name = input("Enter the file name to open: ")
try:
    with open(file_name, 'r') as file:
        content = file.read()
        print(content.title())
except FileNotFoundError:
    print(f"Error: The file '{file_name}' does not exist.")
finally:
    file.close()

# Declare a list with 10 integers and ask the user to enter an index. Check whether the number in that index is positive or negative number. 
# If any invalid index is entered, handle the exception and print an error message.

numbers = [10, -5, 3, 8, -2, 7, 0, -1, 4, 6]
try:
    index = int(input("Enter an index (0-9): "))
    if 0 <= index < len(numbers):
        if numbers[index] >= 0:
            print(f"The number at index {index} is positive: {numbers[index]}")
        else:
            print(f"The number at index {index} is negative: {numbers[index]}")
    else:
        print("Error: Index out of range.")
except ValueError:
    print("Error: Please enter a valid integer index.")
