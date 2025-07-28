# Write a LC program to create an output dictionary which contains only the odd numbers 
# that are present in the input list = [1,2,3,4,5,6,7] as keys and their cubes as values

lst = [1, 2, 3, 4, 5, 6, 7]
output_dict = {x: x**3 for x in lst if x % 2 != 0}
print(output_dict)


# Make a dictionary of the 26 english alphabets mapping each with the corresponding integer

import string
alphabet_dict = {char: idx + 1 for idx, char in enumerate(string.ascii_lowercase)}
print(alphabet_dict)