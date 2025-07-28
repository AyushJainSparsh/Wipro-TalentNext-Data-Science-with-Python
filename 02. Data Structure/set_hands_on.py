# Write a program to remove a given item from the set

set1 = {1, 2, 3, 4, 5}
print("Original set:", set1)
set1.remove(3)
print("Set after removing 3:", set1)

# Write a program to create an intersection of sets.

set2 = {3, 4, 5, 6, 7}
set3 = {5, 6, 7, 8, 9}
intersection_set = set2.intersection(set3)
print("Intersection of set2 and set3:", intersection_set)

# Write a program to create an union of sets.

set4 = {1, 2, 3}
set5 = {3, 4, 5}
union_set = set4.union(set5)
print("Union of set4 and set5:", union_set)

# Write a program to find the maximum and minimum value in a set.

set6 = {10, 20, 30, 40, 50}
max_value = max(set6)
min_value = min(set6)
print("Maximum value in set6:", max_value)
print("Minimum value in set6:", min_value)