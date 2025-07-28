'''
Tech Module:Data Structure

Project: 1 
Create a dictionary that contains a list of people and one interesting fact about each of them.
Display each person and his or her interesting fact to the screen. Next, change a fact about one 
of the people. Also add an additional person and corresponding fact. Display the new list of 
people and facts. Run the program multiple times and notice if the order changes.
Sample :
Input : 
Jeff: Is afraid of Dogs.
David: Plays the piano.
Jason: Can fly an airplane

Output :
jeff: Is afraid of heights.
David: Plays the piano.
Jason: Can fly an airplane.
Jill: Can hula dance
'''

people_facts = {}s
print("Enter 3 people and an interesting fact about each:")

for i in range(3):
    name = input(f"Enter name {i+1}: ")
    fact = input(f"Enter a fact about {name}: ")
    people_facts[name] = fact
print("\nInitial list of people and their facts:")
for person, fact in people_facts.items():
    print(f"{person}: {fact}")

person_to_update = input("\nEnter the name of the person whose fact you'd like to change: ")
new_fact = input(f"Enter the new fact for {person_to_update}: ")
people_facts[person_to_update] = new_fact

new_person = input("\nEnter the name of an additional person: ")
new_person_fact = input(f"Enter a fact about {new_person}: ")
people_facts[new_person] = new_person_fact

print("\nUpdated list of people and their facts:")
for person, fact in people_facts.items():
    print(f"{person}: {fact}")

'''
Project: 2
Given the participant’s score sheet for your University Sports Day, you are required to find the 
runner-up score. You have scores. Store them in a list and find the score of the runner-up.
Sample input:[2, 3, 6, 6, 5]
Sample output: 5
Explanation: Given list is [2, 3, 6, 6, 5]. The maximum score is 6, second maximum is 5. Hence, we 
print 5 as the runner-up score
'''

scores = [int(x) for x in input("Enter scores separated by space: ").split()]
if len(scores) < 2:
    print("Not enough scores to determine a runner-up.")
else:
    unique_scores = list(set(scores))
    unique_scores.sort(reverse=True)
    if len(unique_scores) < 2:
        print("Not enough unique scores to determine a runner-up.")
    else:
        runner_up_score = unique_scores[1]
        print(f"The runner-up score is: {runner_up_score}")

'''
Project: 3
You have a record of n students. Each record contains the student's name, and their percent marks in 
Math, Physics and Chemistry. The marks can be floating values.You are required to save the record in a 
dictionary data type.Student’s name is the key. Marks stored in a list is the value. The userenters a 
student's name. Output the average percentage marks obtained by that student.
Formula:(sum of marks) / (no of subjects)

Sample input: { 
“Krishna” : [67,68,69],
“Arjun” :[70,98,63],
“Malika” : [52,56,60] }
Sample output:
Enter a name: Malika
Average percentage mark: 56 
Explanation:Marks for Malika are [52, 56, 60] whose average is(52 + 56 + 60)/3 => 56
'''

n= int(input("Enter the number of students: "))
students = {}
for _ in range(n):
    name = input("Enter student's name: ")
    marks = list(map(float, input(f"Enter marks for {name} separated by space: ").split()))
    students[name] = marks
student_name = input("Enter a student's name to find their average percentage marks: ")
if student_name in students:
    marks = students[student_name]
    average_marks = sum(marks) / len(marks)
    print(f"Average percentage mark for {student_name}: {average_marks:.2f}")

'''
Project: 4
Given a string of n words, help Alex to find out how many times his name appears in the string. 
Constraint:1 <= n <= 200
Sample input:Hi Alex Welcome Alex Bye Alex.
Sample output:3
Explanation:Alex name appears 3 times in the string. Hi AlexWelcomeAlexBye Alex.
'''

words = input("Enter a string of words: ").split()
name_to_count = "Alex"
count = words.count(name_to_count)
print(f"The name '{name_to_count}' appears {count} times in the string.")