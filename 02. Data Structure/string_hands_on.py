# Write a program to count the number of upper and lower case letters in a String.

sent = input("Enter a string: ")
upper_count = 0
lower_count = 0
for char in sent:
    if char.isupper():
        upper_count += 1
    elif char.islower():
        lower_count += 1
print("Number of uppercase letters:", upper_count)
print("Number of lowercase letters:", lower_count)

# Write a program that will check whether a given String is Palindrome or not.

sent1 = input("Enter a string to check for palindrome: ")
if sent1 == sent1[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

# Given a string, return a new string made of n copies of the first 2 chars of the 
# original string where n is the length of the string. The string length will be >=2. 
# If input is "Wipro" then output should be "WiWiWiWiWi".

sent2 = input("Enter a string for n copies: ")
n = len(sent2)
first_two_chars = sent2[:2]
result = first_two_chars * n
print("Resulting string:", result)

# Given a string, if the first or last character is 'x', return the string without 
# those 'x' character, else return the string unchanged. If the input is "xHix", then output is "Hi".

sent3 = input("Enter a string to check for 'x': ")
if sent3.startswith('x'):
    sent3 = sent3[1:]
if sent3.endswith('x'):
    sent3 = sent3[:-1]
print("Modified string:", sent3)

# Given a string and an integer n, return a string made of n repetitions of the last n 
# characters of the string. You may assume that n is between 0 and the length of the string 
# inclusive. 
# For example if the inputs are “Wipro” and 3, then the output should be “propropro”.

sent4 = input("Enter a string for last n characters: ")
n = int(input("Enter an integer n: "))
if n > 0 and n <= len(sent4):
    last_n_chars = sent4[-n:]
    result_n_repeats = last_n_chars * n
    print("Resulting string:", result_n_repeats)
else:
    print("Invalid value for n. It should be between 0 and the length of the string inclusive.")