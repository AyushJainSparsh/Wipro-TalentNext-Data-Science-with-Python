'''
Tech Module: Command Line Arguments
Project: 1

Through command line arguments three strings separated by space aregiven to you. 
Eachstring is a series of numbersseparated by hyphen(-). You like all the numbers 
in string 1 and dislike all the numbers in string 2.
Third string contains thenumbers given to you. Your initial happiness is 0. When 
you encounter anumberwhich is present in string 1, add 1 to yourhappiness, if it 
is present in string 2, add -1 to your happiness.Otherwise, your happiness does 
not change.Output your final happiness at the end.

Sample input 1:3-15-7 1-5-3-8
Sample output 1:1
Explanation:
Numbers in string 1: 3, 1
Numbers in string 2: 5, 7
Numbers given to you: 1, 5, 3, 8
You gain 1 unit of happiness for numbers 1 and 3 which are in string 1.Your total happiness is 2 now.
You lose 1 unit of happiness for number 5 which is in string 2.Your total happiness in 1 now.
8 is not present in either of the strings, so your happiness does notchange.Final happiness is 1.

Sample input 2:60-77-34-5-2  44-11-99-3 77-15-13-2-34-3
Sample output 2:2
Explanation:
You gain 1 unit of happiness for numbers 77, 2 and 34which are in string 1.Your total happiness is 3now.
You lose 1 unit of happiness for number 3which is in string 2.Your total happiness in 2now.
15 and 13 arenot present in either of the strings, so your happiness does not change.
Final happiness is 2
'''

import sys
def calculate_happiness(like_str, dislike_str, numbers_str):
    like_numbers = set(map(int, like_str.split('-')))
    dislike_numbers = set(map(int, dislike_str.split('-')))
    numbers = map(int, numbers_str.split('-'))

    happiness = 0
    for number in numbers:
        if number in like_numbers:
            happiness += 1
        elif number in dislike_numbers:
            happiness -= 1

    return happiness

like_str = sys.argv[1]
dislike_str = sys.argv[2]
numbers_str = sys.argv[3]
final_happiness = calculate_happiness(like_str, dislike_str, numbers_str)
print(final_happiness)