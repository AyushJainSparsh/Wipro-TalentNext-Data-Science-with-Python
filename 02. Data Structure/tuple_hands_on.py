#  Write a program to print the 4th element from first and 4th element from last in a tuple.

touple = (10, 20, 30, 40, 50, 60, 70, 80, 90)
print("4th element from first:", touple[3])
print("4th element from last:", touple[-4])

# Write a program to check whether an element exists in a tuple or not.

element = int(input("Enter an element to check: "))
if element in touple:
    print(f"{element} exists in the tuple.")
else:
    print(f"{element} does not exist in the tuple.")

# Write a program to convert a list into a tuple.

list_data = [1, 2, 3, 4, 5]
tuple_data = tuple(list_data)
print("Converted tuple:", tuple_data)
print("Type of converted data:", type(tuple_data))

# Write a program to find the index of an item in a tuple.

touple = (10, 20, 30, 40, 50)
item = int(input("Enter an item to find its index: "))
if item in touple:
    index = touple.index(item)
    print(f"Index of {item} in the tuple is: {index}")

# Write a program to replace last value of tuples in a list to 100.  
# Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)] 
# Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]

list_of_tuples = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
print("Original list of tuples:", list_of_tuples)
updated_list = [t[:-1] + (100,) for t in list_of_tuples]
print("Updated list of tuples:", updated_list)