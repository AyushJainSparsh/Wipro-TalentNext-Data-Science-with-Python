# Write a program to add a key and value to a dictionary.   
# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}

sample_dict = {0: 10, 1: 20}
sample_dict[2] = 30
print(sample_dict)

# Write a program to concatenate the following dictionaries to create a new one.  
# Sample Dictionary : 
# dic1={1:10, 2:20}  dic2={3:30, 4:40}  dic3={5:50,6:60} 
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
new_dict = {**dic1, **dic2, **dic3}
print(new_dict)

# Write a program to check if a given key already exists in a dictionary.

sample_dict = {0: 10, 1: 20}
key_to_check = 1
if key_to_check in sample_dict:
    print(f"Key {key_to_check} exists in the dictionary.")
else:
    print(f"Key {key_to_check} does not exist in the dictionary.")

# Write a program to iterate over a dictionary using for loop and print the keys alone, values alone and both keys and values.

sample_dict = {0: 10, 1: 20, 2: 30}
print("Keys:")
for key in sample_dict.keys():
    print(key)
print("Values:")
for value in sample_dict.values():
    print(value)
print("Keys and Values:")
for key, value in sample_dict.items():
    print(f"{key}: {value}")

# Write a program to prepare a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of the keys.

sample_dict = {i: i**2 for i in range(1, 16)}
print(sample_dict)

# Write a program to sum all the values in a dictionary, considering the values will be of int type.

sample_dict = {0: 10, 1: 20, 2: 30}
total_sum = sum(sample_dict.values())
print(f"Total sum of values: {total_sum}")