# Write a program to create a list of 5 integers and display the list items. Access individual elements through index.

list_items = [1, 2, 3, 4, 5]
for i in range(len(list_items)):
    print(f"Element at index {i}: {list_items[i]}")

# Write a program to append a new item to the end of the list.

list_items.append(6)
print("List after appending a new item:", list_items)

# Write a program to reverse the order of the items in the list.

print("List before reversing:", list_items)
list_items.reverse()
print("List after reversing:", list_items)

# Write a program to print the number of occurrences of a specified element in a list.

element = int(input("Enter an element to count its occurrences: "))
count = list_items.count(element)   
print(f"The element {element} occurs {count} times in the list.")

# Write a program to append the items of list1 to list2 in the front.

list1 = [7, 8, 9]
print("List1:", list1)
list2 = [10, 11, 12]
print("List2 before appending:", list2)
list2 = list1 + list2
print("List2 after appending items of List1 in front:", list2)

# Write a program to insert a new item before the second element in an existing list.

list_items = [1, 2, 3, 4, 5]
print("Original List:", list_items)
list_items.insert(1, 99)
print("List after inserting a new item before the second element:", list_items)

# Write a program to remove the item from a specified index in a list.

item = int(input("Enter the index of the item to remove: "))
if 0 <= item < len(list_items):
    removed_item = list_items.pop(item)
    print(f"Removed item: {removed_item}")

# Write a program to remove the first occurrence of a specified element from a list.

element = int(input("Enter an element to remove its first occurrence: "))
if element in list_items:
    list_items.remove(element)
    print(f"List after removing the first occurrence of {element}:", list_items)