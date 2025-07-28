# Write a program to read the entire content from a txt file and display it to the user.

with open('sample.txt', 'r') as file:
    content = file.read()
    print(content)
file.close()

# Write a program to read first n lines from a txt file. Get n as user input.

n = int(input("Enter the number of lines to read: "))
with open('sample.txt', 'r') as file:
    for _ in range(n):
        line = file.readline()
        if not line:
            break
        print(line.strip())
file.close()

# Write a program to accept input from user and append it to a txt file.

user_input = input("Enter text to append to the file: ")
with open('sample.txt', 'a') as file:
    file.write(user_input + '\n')
file.close()

# Write a program to read contents from a txt file line by line and store each line into a list.

with open('sample.txt', 'r') as file:
    lines = file.readlines()
    lines_list = [line.strip() for line in lines]
    print(lines_list)
file.close()

# Write a program to find the longest word from the txt file contents, assuming that the file will have only one longest word in it.

with open('sample.txt', 'r') as file:
    words = file.read().split()
    longest_word = max(words, key=len)
    print("Longest word:", longest_word)
file.close()

# Write a program to count the frequency of a user entered word in a txt file.

user_word = input("Enter a word to count its frequency: ")
with open('sample.txt', 'r') as file:
    content = file.read()
    frequency = content.lower().split().count(user_word.lower())
    print(f"The word '{user_word}' appears {frequency} times in the file.")
file.close()