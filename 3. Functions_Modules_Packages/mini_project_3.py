'''
Tech Module: Functions/Modules/Packages
Project: 1
Write a Python functionthat accepts a hyphen-separated sequence of colors as input 
and returns the colors in a hyphen-separated sequence after sorting them alphabetically.
Constraint:All the colors will be completely in either lower case or upper case.

Sample input1:green-red-yellow-black-white
Sample output1:black-green-red-white-yellow

Sample input2:PINK-BLUE-TAN-PURPLE
Sample output2:BLUE-PINK-PURPLE-TAN

'''

def sort_colors(color_string):
    colors = color_string.split('-')
    sorted_colors = sorted(colors)
    return '-'.join(sorted_colors)

list_of_colors = input("Enter colors separated by hyphen: ")
print(sort_colors(list_of_colors))

'''
Project: 2
Create a Python module with the following functions:
Function Name Task ispalindrome(name)
Given the user name as input, this function should tell us whether the name is a palindrome or not.
count_the_vowels(name)Given the user name as input, this function should tell us howmany vowels are present in it.
frequency_of_letters(name)Given the user name as input, this function should tell us 
how many times each letter appears in the name.

Note:name will be completely in either lower case or upper case.
Import the module in another python script and test the functions by passing appropriate inputs.

Sample input1:bob
Sample output 1:Yes it is a palindrome.
No of vowels: 1
Frequency of letters: b-2, o-1

Sample input2:marcelbentok tanakaSample 
utput 2:Noit is not a palindrome.
No of vowels: 7
Frequency of letters: m-1, a-4, r-1, c-1, e-2, l-1, b-1, n-2, t-2, o-1,k-2
'''

def is_palindrome(name):
    name = name.lower()
    return name == name[::-1]
def count_the_vowels(name):
    vowels = 'aeiou'
    count = sum(1 for char in name.lower() if char in vowels)
    return count
def frequency_of_letters(name):
    frequency = {}
    for char in name.lower():
        if char.isalpha():  # Count only alphabetic characters
            frequency[char] = frequency.get(char, 0) + 1
    return frequency

name = input("Enter your name: ")
if is_palindrome(name):
    print("Yes it is a palindrome.")
else:
    print("No it is not a palindrome.")
print("No of vowels:", count_the_vowels(name))
freq = frequency_of_letters(name)
freq_output = ', '.join(f"{char}-{count}" for char, count in freq.items())
print("Frequency of letters:", freq_output)